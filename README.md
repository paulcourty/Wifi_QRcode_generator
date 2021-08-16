<h1>Wifi QR codes</h1>

<br/>

I wrote simple script to generate Wifi QRcodes. 

It's practical for friends coming over, they can now connect to the wifi within seconds taking a picture !

<br/>

The `wifi_qrcode.ipynb` Notebook & `wifi_qrcode.py` Python scripts essentially do the same thing, so run the one that you're most comfortable with. Both try to retrieve your wifi information directly from your laptop, otherwise they ask you to type the info manually.

<br/>

Here is an example of the output:

![Wifi QRcode Example](https://github.com/paulcourty/Wifi_QRcode_generator/blob/main/Wifi%20Random.png)

---

You can run the `wifi_qrcode.py` script yourself by simply cloning this repository (`git` or manually downloading the folder). Then, go into a terminal, navigate to the cloned repository, and install the necessary Python dependencies:

```sh
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

Then, run the Python script:

```sh
python wifi_qrcode.py
```
