# Idiosyncrasies

## Format

1. Python function
2. Classification of function: idiosyncratic or general
3. Reason for classification

## Examples

```python
def get_label(code='', label=''):
    if code is None:
        code = '-'
    if label is None:
        label = 'inconnu'
    return f'{code} {label[:30]}'
```

- idiosyncratic
- "inconnu" is a French word, and the function is not generalizable to other languages.

---

```python
def train_core(domain: Union[Domain, Text], config: Text, stories: Text, output: Text, train_path: Optional[Text]=None, fixed_model_name: Optional[Text]=None, additional_arguments: Optional[Dict]=None) -> Optional[Text]:
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(train_core_async(domain=domain, config=config, stories=stories, output=output, train_path=train_path, fixed_model_name=fixed_model_name, additional_arguments=additional_arguments))
```

- general
- ML training is a generalizable task, and this function can be applied to many other ML training tasks.

---

```python
def train(domain: Text, config: Text, training_files: Union[Text, List[Text]], output: Text=DEFAULT_MODELS_PATH, force_training: bool=False, fixed_model_name: Optional[Text]=None, persist_nlu_training_data: bool=False, additional_arguments: Optional[Dict]=None, loop: Optional[asyncio.AbstractEventLoop]=None) -> Optional[Text]:
    if loop is None:
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
    return loop.run_until_complete(train_async(domain=domain, config=config, training_files=training_files, output_path=output, force_training=force_training, fixed_model_name=fixed_model_name, persist_nlu_training_data=persist_nlu_training_data, additional_arguments=additional_arguments))
```

- general
- ML training is a generalizable task, and this function can be applied to many other ML training tasks.

---

```python
def train_nlu(config: Text, nlu_data: Text, output: Text, train_path: Optional[Text]=None, fixed_model_name: Optional[Text]=None, persist_nlu_training_data: bool=False) -> Optional[Text]:
    """Trains an NLU model.

    Args:
        config: Path to the config file for NLU.
        nlu_data: Path to the NLU training data.
        output: Output path.
        train_path: If `None` the model will be trained in a temporary
            directory, otherwise in the provided directory.
        fixed_model_name: Name of the model to be stored.
        persist_nlu_training_data: `True` if the NLU training data should be persisted
                                   with the model.


    Returns:
        If `train_path` is given it returns the path to the model archive,
        otherwise the path to the directory with the trained model files.

    """
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(_train_nlu_async(config, nlu_data, output, train_path, fixed_model_name, persist_nlu_training_data))
```

- general
- ML training is a generalizable task, and this function can be applied to many other ML training tasks.

---

```python
def pnasnet_A(data_channel):
    model = PNASNet(data_channel=data_channel, num_cells=6, num_planes=44, block=CellA)
    model.set_name(BackboneName.PNASNetA)
    return model
```

- general
- PNASNet is some kind of ML model, and this function simply returns an instance of it after setting some parameters.

---

```python
def pnasnet_B(data_channel):
    model = PNASNet(data_channel=data_channel, num_cells=6, num_planes=32, block=CellB)
    model.set_name(BackboneName.PNASNetB)
    return model
```

- general
- PNASNet is some kind of ML model, and this function simply returns an instance of it after setting some parameters.

---

```python
def get_access_token(token):
    resp = None
    request_count = 0
    url = 'https://api.cesium.com/v1/assets/1/endpoint'
    while True:
        if request_count > 4:
            break
        try:
            request_count += 1
            param = {'access_token': token}
            resp = requests.get(url, params=param, timeout=2)
            if resp.status_code != 200:
                continue
            break
        except Exception as e:
            resp = None
            time.sleep(3)
    if resp is None:
        return None
    resp_json = resp.json()
    return resp_json.get('accessToken')
```

- general
- This function is a wrapper for a REST API call, and it can be applied to many other REST API calls.

---

```python
def download_file_W(pdf_url, mdir, filename, flag=False):
    filename = mdir + filename
    ssl._create_default_https_context = ssl._create_unverified_context
    wget.download(pdf_url, filename)
    if os.stat(filename).st_size == 0:
        flag = 0
    else:
        flag = 1
    return flag
```

- general
- This function is a wrapper for a file download, and it can be applied to many other file downloads.

---

```python
def is_valid_pdf(fn):
    """Check is the PDF valid """
    try:
        with open(fn, 'rb') as f:
            pdf = PdfFileReader(f)
            numpages = pdf.numPages
        return numpages > 0
    except Exception as e:
        return False
```

- general
- This function checks how many pages a PDF file has, and it can be applied to many other PDF files.

---

```python
def download_file(pdf_url, mdir, filename, flag=False):
    if flag is True:
        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(pdf_url, context=context)
    else:
        response = urllib.request.urlopen(pdf_url)
    filename = mdir + filename
    file = open(filename, 'wb')
    file.write(response.read())
    if os.stat(filename).st_size == 0:
        flag = 0
    else:
        flag = 1
    file.close()
    return flag
```

- general
- This function is a wrapper for a file download, and it can be applied to many other file downloads.

---

```python
def getDriver(url):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver
```

- general
- This function returns a driver for a web browser.

---

```python
def cosine_dist(x, y):
    """Computes Cosine Distance."""
    x = F.normalize(x, dim=1)
    y = F.normalize(y, dim=1)
    dist = 2 - 2 * torch.mm(x, y.t())
    return dist
```

- general
- This function computes the cosine distance between two vectors.

---

```python
def normalize(x, axis=-1):
    """Performs L2-Norm."""
    num = x
    denom = torch.norm(x, 2, axis, keepdim=True).expand_as(x) + 1e-12
    return num / denom
```

- general
- This function performs L2-Norm on a vector.

---

```python
def euclidean_dist(x, y):
    """Computes Euclidean distance."""
    m, n = (x.size(0), y.size(0))
    xx = torch.pow(x, 2).sum(1, keepdim=True).expand(m, n)
    yy = torch.pow(x, 2).sum(1, keepdim=True).expand(m, m).t()
    dist = xx + yy - 2 * torch.matmul(x, y.t())
    dist = dist.clamp(min=1e-12).sqrt()
    return dist
```

- general
- This function computes the Euclidean distance between two vectors.

---

```python
def json_decode(json_string):
    try:
        ret = json.loads(json_string)
    except:
        json_string = fix_lazy_json(json_string)
        ret = json.loads(json_string)
    return ret
```

- general
- This function decodes a JSON string.

---

```python
def process_line(line):
    line_sp = line.split(',')
    ques = str(line_sp[1]).strip().upper()
    label = str(line_sp[0]).strip().upper()
    label = 'NAN' if label == '' else label
    que_embed = embed.sentence2idx(ques)
    label_zeros = [0] * len(l2i_i2l['l2i'])
    label_zeros[l2i_i2l['l2i'][label]] = 1
    return (que_embed, label_zeros)
```

- idiosyncratic
- This function assumes the input to be of a specific format which is unclear from the code.

---

```python
def jisuan(str_num):
    he1 = 0
    global out_l1
    for i in l1():
        he1 += int(i) ** 2
    if he1 > int(str_num):
        out_l1.append(str_num)
    return None
```

- idiosyncratic
- "jisuan" means "calculate" in Chinese, but what it calculates is unclear from the code.

---
