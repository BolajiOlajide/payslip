# Payslip

## Setup

* Ensure Python 3.5+ is installed on your machine

* Clone the repository with the command

```bash
git clone https://github.com/BolajiOlajide/payslip.git
```

* Navigate to the project with the command

```bash
cd payslip
```

* Install the dependencies with the command

```bash
pip install -r requirements.txt
```

### Scraping

Everything should be ready to go once the dependencies have been installed. To start scraping, simply run the command:

```bash
python main.py
```

You'll receive a prompt to enter the email sender whose email you'll love to scrape - if you're using this for the purpose of scraping payslips it should be the financial service handling your company's compensation thingy.

Anyways once you've entered a valid email, it should begin scraping and you should ideally find your files in the `attachments` directory.

Gracias!
