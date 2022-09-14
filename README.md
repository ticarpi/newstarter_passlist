# Generate New Starter Password List

Similar to [http://weakpasswords.net/](http://weakpasswords.net/), this creates a list of probable passwords for new starters in an AD environment. It uses the current data settings, but can also be extended to 'backdate' potential passwords for accounts created earlier. It can also be augmented to use additional custom words, such as the name of the company.

---

## Examples:
Generate common passwords with a depth/age of 3 years:  
`.\newstarter_passlist.py -d 3`

Generate common passwords for a specific company/domain target:  
`.\newstarter_passlist.py -a companyname -a companylocation -a businesstype`

Generate common passwords and output to a file:  
`.\newstarter_passlist.py -o newstarter_yy.lst`

---

## Usage

```
usage: newstarter_passlist.py [-h] [-o OUTPUTFILE] [-d DEPTH] [-a ADDITIONALWORDS]

Generate password lists for commonly set New Starter account passwords.

options:
  -h, --help            show this help message and exit
  -o OUTPUTFILE, --outputfile OUTPUTFILE
                        name of the output list
  -d DEPTH, --depth DEPTH
                        how many years to backdate the search
  -a ADDITIONALWORDS, --additionalwords ADDITIONALWORDS
                        words to add to the existing common base words list. For example: company name, office
                        location. Note: can add multiple
```
