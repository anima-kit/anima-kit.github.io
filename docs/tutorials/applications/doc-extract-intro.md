---
title: Data Extraction
template: pages.html
---

<div class="icon-def-1" style="text-align: center; border: 0.1rem dotted; width: 5%; float: right; padding: 0px; margin: 0px; font-size: 0.9rem; border-radius: 10px;">
  <a onclick="toggleAnimations()" title="Toggle Animations" style="cursor: pointer;">
    <p style="padding: 0px; margin: 0px;"><i class="mdi mdi-sine-wave"></i></p>
  </a>
</div>

# :material-file-document-multiple-outline:{ .icon-def-0 } Intro to Document Extraction with Docling

<hr class="icon-def-1 tertiary-icon", style="width: 90%;"> 

:material-fire:{.icon-def-0} Docling's [document extraction module](https://github.com/docling-project/docling/blob/main/docling/document_extractor.py) is super powerful. :material-fire:{.icon-def-0} 

It uses the [NuExtract model](https://huggingface.co/numind/NuExtract-2.0-8B) to obtain structured data from unstructured documents (currently PDFs and images) through defining templates for the desired data. 

By defining the data templates in clever ways, we can potentially extract lots of various information from a wide range of documents. This is exactly what we'll see as we go through the tutorials.

To start off, we're going to go through some simple examples of extracting information using a [Kaggle dataset of scanned receipts](https://www.kaggle.com/datasets/jenswalter/receipts). 

So, let's get started! 

<hr class="icon-def-1 primary-icon", style="width: 90%;"> 

## Setup

First, we're going to import all the libraries that we'll need.


```python
## Import all the necessary libraries
import os
import zipfile
from IPython import display
from rich import print
from typing import Optional, List
from pydantic import BaseModel, Field, root_validator
from docling.datamodel.base_models import InputFormat
from docling.document_extractor import DocumentExtractor
```

Now that we've imported everything, let's setup our data from Kaggle. We'll download our dataset, then create a [Pandas](https://pandas.pydata.org/) dataframe to easily visualize and work with the data.

<hr class="icon-def-1 primary-icon", style="width: 60%;"> 

### Get dataset from Kaggle

First, we'll create the local folder to hold the data, then download the dataset from Kaggle.


```python
## Define file path to the data folder
file_path = '../../data/receipts'

## Create the data folder if it doesn't exist
if not os.path.exists(file_path):
    os.makedirs(file_path)
```


```python
## Use Kaggle API to download the dataset to the data folder
!kaggle datasets download -d jenswalter/receipts -p ../../data/receipts
```

``` title="Ouput"
Dataset URL: https://www.kaggle.com/datasets/jenswalter/receipts
License(s): CC0-1.0
receipts.zip: Skipping, found more recently modified local copy (use --force to force download)
```
    

Now, we can extract the `.zip` file to get the underlying `.pdfs` from which we'll extract relevant data.


```python
## Extract the .pdf files to the data folder
zip_file_path = os.path.join(file_path, 'receipts.zip')
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(file_path)
```

Notice that we now have lots of different receipts corresponding to different dates, locations, and services. What a great dataset to try to extract relevant data from! ✨

Let's checkout one of the receipts:


```python
receipt_file = os.path.join(file_path, "2024/us/luckylouie_20240529_001.pdf")
```

![receipt](https://anima-kit.github.io/ai-notebooks/assets/receipt.jpg){.img-def}

Now, we can see what type of data we might want to extract. To name a few - there's price info like total, subtotal, tax, tip; purchased item info like name, quantity, and price; establishment info like name and address; and payment method info like card transactions. In these tutorials, we'll see that this info can be extracted from a wide range of receipts quickly and easily with Docling.

Let's start simple, then we can add more complexity as we better understand how to get things working. 

<hr class="icon-def-1 primary-icon", style="width: 90%;"> 

## Extraction

First, let's see how to define the `extractor` object in Docling.


```python
extractor = DocumentExtractor(
    allowed_formats=[InputFormat.IMAGE, InputFormat.PDF],
)
```

Here, we're using Docling's [DocumentExtractor](https://github.com/docling-project/docling/blob/main/docling/document_extractor.py) which can take in a number of allowed input formats. As of writing this, the only allowed formats are PDFs and images, so let's add them both.

If you look at the source code for the class, you'll see that it has two external methods that we can use for extraction: the `extract` method for a single PDF or image; and the `extract_all` method for iterative extraction of multiple sources.

As a first example, let's use the `extract` method on our example receipt. We need to pass this method a `template` which defines the information that we want to extract. An easy way to do this is by creating a dictionary:


```python
## Create a dictionary defining the price total by giving it a `name` and a `type`
target_data = {'total': 'float'}
```


```python
## Extract the target data from the receipt
result = extractor.extract(
    source=receipt_file,
    template=target_data,
)
print(result)
```   

<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800080; text-decoration-color: #800080; font-weight: bold">ExtractionResult</span><span style="font-weight: bold">(</span>
    <span style="color: #808000; text-decoration-color: #808000">input</span>=<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">InputDocument</span><span style="font-weight: bold">(</span>
        <span style="color: #808000; text-decoration-color: #808000">file</span>=<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">PureWindowsPath</span><span style="font-weight: bold">(</span><span style="color: #008000; text-decoration-color: #008000">'luckylouie_20240529_001.pdf'</span><span style="font-weight: bold">)</span>,
        <span style="color: #808000; text-decoration-color: #808000">document_hash</span>=<span style="color: #008000; text-decoration-color: #008000">'422ee7a6a8115deb39be771a95f0c3e9b0fc8af151f37c53fb8cde7e59c0282b'</span>,
        <span style="color: #808000; text-decoration-color: #808000">valid</span>=<span style="color: #00ff00; text-decoration-color: #00ff00; font-style: italic">True</span>,
        <span style="color: #808000; text-decoration-color: #808000">backend_options</span>=<span style="color: #800080; text-decoration-color: #800080; font-style: italic">None</span>,
        <span style="color: #808000; text-decoration-color: #808000">limits</span>=<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">DocumentLimits</span><span style="font-weight: bold">(</span>
            <span style="color: #808000; text-decoration-color: #808000">max_num_pages</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">9223372036854775807</span>,
            <span style="color: #808000; text-decoration-color: #808000">max_file_size</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">9223372036854775807</span>,
            <span style="color: #808000; text-decoration-color: #808000">page_range</span>=<span style="font-weight: bold">(</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">9223372036854775807</span><span style="font-weight: bold">)</span>
        <span style="font-weight: bold">)</span>,
        <span style="color: #808000; text-decoration-color: #808000">format</span>=<span style="font-weight: bold">&lt;</span><span style="color: #ff00ff; text-decoration-color: #ff00ff; font-weight: bold">InputFormat.PDF:</span><span style="color: #000000; text-decoration-color: #000000"> </span><span style="color: #008000; text-decoration-color: #008000">'pdf'</span><span style="color: #000000; text-decoration-color: #000000">&gt;,</span>
<span style="color: #000000; text-decoration-color: #000000">        </span><span style="color: #808000; text-decoration-color: #808000">filesize</span><span style="color: #000000; text-decoration-color: #000000">=</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">40278</span><span style="color: #000000; text-decoration-color: #000000">,</span>
<span style="color: #000000; text-decoration-color: #000000">        </span><span style="color: #808000; text-decoration-color: #808000">page_count</span><span style="color: #000000; text-decoration-color: #000000">=</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>
<span style="color: #000000; text-decoration-color: #000000">    </span><span style="color: #000000; text-decoration-color: #000000; font-weight: bold">)</span><span style="color: #000000; text-decoration-color: #000000">,</span>
<span style="color: #000000; text-decoration-color: #000000">    </span><span style="color: #808000; text-decoration-color: #808000">status</span><span style="color: #000000; text-decoration-color: #000000">=&lt;ConversionStatus.SUCCESS: </span><span style="color: #008000; text-decoration-color: #008000">'success'</span><span style="font-weight: bold">&gt;</span>,
    <span style="color: #808000; text-decoration-color: #808000">errors</span>=<span style="font-weight: bold">[]</span>,
    <span style="color: #808000; text-decoration-color: #808000">pages</span>=<span style="font-weight: bold">[</span><span style="color: #800080; text-decoration-color: #800080; font-weight: bold">ExtractedPageData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">page_no</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>, <span style="color: #808000; text-decoration-color: #808000">extracted_data</span>=<span style="font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'total'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">29.28</span><span style="font-weight: bold">}</span>, <span style="color: #808000; text-decoration-color: #808000">raw_text</span>=<span style="color: #008000; text-decoration-color: #008000">'{"total": 29.28}'</span>, <span style="color: #808000; text-decoration-color: #808000">errors</span>=<span style="font-weight: bold">[])]</span>
<span style="font-weight: bold">)</span>
</pre>



We see that the result gives a lot of information about the document that we processed and the pipeline that we used. It also gives the extracted data from each of the input pages. Let's look at the data it extracted more closely:


```python
for page in result.pages:
    print(page.extracted_data)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'total'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">29.28</span><span style="font-weight: bold">}</span>
</pre>



Yep, looks like it works! What about adding the subtotal to the target data?


```python
target_data = {
    'total': 'float',
    'subtotal': 'float'
}

result = extractor.extract(
    source=receipt_file,
    template=target_data,
)

for page in result.pages:
    print(page.extracted_data)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'total'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">29.28</span>, <span style="color: #008000; text-decoration-color: #008000">'subtotal'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">22.49</span><span style="font-weight: bold">}</span>
</pre>



Still working great! Seems like it can tell the difference between `total` and `subtotal` without much guidance. But, what about something that isn't explicitly written on the receipt, like customer (I assume that's Tony)?


```python
target_data = {
    'total': 'float',
    'subtotal': 'float',
    'customer': 'str'
}

result = extractor.extract(
    source=receipt_file,
    template=target_data,
)

for page in result.pages:
    print(page.extracted_data)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'total'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">29.28</span>, <span style="color: #008000; text-decoration-color: #008000">'subtotal'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">22.49</span>, <span style="color: #008000; text-decoration-color: #008000">'customer'</span>: <span style="color: #008000; text-decoration-color: #008000">'Tony'</span><span style="font-weight: bold">}</span>
</pre>



Ha! 😂 What a boss. If it can do that, extracting the server as well is probably doable:


```python
target_data = {
    'total': 'float',
    'subtotal': 'float',
    'customer': 'str',
    'server': 'str'
}

result = extractor.extract(
    source=receipt_file,
    template=target_data,
)

for page in result.pages:
    print(page.extracted_data)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'total'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">29.28</span>, <span style="color: #008000; text-decoration-color: #008000">'subtotal'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">22.49</span>, <span style="color: #008000; text-decoration-color: #008000">'customer'</span>: <span style="color: #008000; text-decoration-color: #008000">'Tony'</span>, <span style="color: #008000; text-decoration-color: #008000">'server'</span>: <span style="color: #008000; text-decoration-color: #008000">'Rosina R'</span><span style="font-weight: bold">}</span>
</pre>



There we go. How awesome is that? There's so much power here and it's so simple to use!

Let's add a bit more control by using [Pydantic](https://docs.pydantic.dev/latest/) to describe our target data instead of a simple dictionary. We can define a specific `Receipt` class as a `BaseModel` with `Fields` describing our target data pieces:


```python
class Receipt(BaseModel):
    total: float = Field(
        default=None, 
        examples=[10]
    )
    subtotal: Optional[float] = Field(
        default=None, 
        examples=[10]
    )
    customer: Optional[float] = Field(
        default=None, 
        examples=["Anima"]
    )
    server: Optional[float] = Field(
        default=None, 
        examples=["Anima"]
    )
```

I've defined all the target values that we used earlier with `None` default values and a example for each. Also, everything but the total is taken as optional, since not all receipts will have the relevant information.

> From what I can tell, adding a `description` argument to the `Field` doesn't do anything. See the `ExtractionTemplateFactory` class [here](https://github.com/docling-project/docling/blob/4852d8b4f2938434f1d6250984fa18ec5428055f/docling/pipeline/extraction_vlm_pipeline.py) for more details.

Now we can pass in our `Receipt` model to the extractor:


```python
result = extractor.extract(
    source=receipt_file,
    template=Receipt,
)

for page in result.pages:
    print(page.extracted_data)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'total'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">29.28</span>, <span style="color: #008000; text-decoration-color: #008000">'subtotal'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">22.49</span>, <span style="color: #008000; text-decoration-color: #008000">'customer'</span>: <span style="color: #008000; text-decoration-color: #008000">'Tony'</span>, <span style="color: #008000; text-decoration-color: #008000">'server'</span>: <span style="color: #008000; text-decoration-color: #008000">'Rosina R'</span><span style="font-weight: bold">}</span>
</pre>



Great, looks like it's still working! We'll be able to control our target data a bit more with this method. We can define as many `BaseModels` as we want and combine them together to get complex structures of target data.

Let's take the purchased items as an example. For each purchased item, we'll want to extract the name, the quantity, and the price of the item. Since we know that receipts will typically list each of the purchased items, we can first define a `PurchasedItem` model, then add a list of `purchased_items` to our `Receipt` model.


```python
## Define the PurchasedItem model describing a single item listed on the reciept
class PurchasedItem(BaseModel):
    name: Optional[str] = Field(
        default=None, 
        examples=["Item"]
    )
    quantity: Optional[int] = Field(
        default=None, 
        examples=[1]
    )
    price: Optional[float] = Field(
        default=None, 
        examples=[10]
    )

## Now add a `purchased_items` variable from the `PurchasedItem` model
class Receipt(BaseModel):
    total: float = Field(
        default=None, 
        examples=[10]
    )
    subtotal: Optional[float] = Field(
        default=None, 
        examples=[10]
    )
    customer: Optional[float] = Field(
        default=None, 
        examples=["Anima"]
    )
    server: Optional[float] = Field(
        default=None, 
        examples=["Anima"]
    )
    purchased_items: Optional[List[PurchasedItem]] = Field(
        default=[PurchasedItem()],
        examples=[[PurchasedItem()]]
    )
```

Here, we've defined the `purchased_items` variable as a list of `PurchasedItem` models. We define the default and example as a list of one default `PurchasedItem`. Let's see how it does:


```python
result = extractor.extract(
    source=receipt_file,
    template=Receipt,
)

for page in result.pages:
    print(page.extracted_data)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span>
    <span style="color: #008000; text-decoration-color: #008000">'total'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">29.28</span>,
    <span style="color: #008000; text-decoration-color: #008000">'subtotal'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">22.49</span>,
    <span style="color: #008000; text-decoration-color: #008000">'customer'</span>: <span style="color: #008000; text-decoration-color: #008000">'Tony'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'server'</span>: <span style="color: #008000; text-decoration-color: #008000">'Rosina R'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'purchased_items'</span>: <span style="font-weight: bold">[{</span><span style="color: #008000; text-decoration-color: #008000">'name'</span>: <span style="color: #008000; text-decoration-color: #008000">'1 3 PC Salmon Combo #1'</span>, <span style="color: #008000; text-decoration-color: #008000">'quantity'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>, <span style="color: #008000; text-decoration-color: #008000">'price'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">22.49</span><span style="font-weight: bold">}]</span>
<span style="font-weight: bold">}</span>
</pre>

---

And that's how simple it is to extract complex data from unstructured documents using Docling!

Stay tuned for the next tutorial, where we'll add even more complexity to our model and see how it holds up against different types of receipts. 

<hr class="icon-def-1 primary-icon", style="width: 30%;"> 
