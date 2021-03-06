<h1>Wifi QR codes</h1>

<br/>

I wrote a simple script to generate **Wifi QRcodes**. 

It's practical for friends coming over, they can now connect to the wifi by taking a picture !

<br/>

The scripts try to retrieve your wifi information directly from your laptop, otherwise they ask you to type the info manually. Both `wifi_qrcode.py` & `wifi_qrcode.ipynb` do the same thing, so run the one that you're most comfortable with. 

<br/>

You can run the `wifi_qrcode.py` script by simply cloning this repository (`git` or manually downloading the folder). Then, go into a terminal, navigate to the cloned repository, and install the necessary Python dependencies:

For **Unix/macOS**:

```sh
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

For **Windows**:

```sh
py -m venv .env
.env/Scripts/activate
pip install -r requirements.txt
```

Then, run the Python script:

```sh
python wifi_qrcode.py
```

<br/>

Finally, you should get a QR code (`.png`) of the sort:

![Wifi QRcode Example](https://github.com/paulcourty/Wifi_QRcode_generator/blob/main/Wifi%20Example.png)