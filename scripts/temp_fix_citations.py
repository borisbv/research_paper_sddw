import re
from pathlib import Path

# Mapping of patterns to [@bibkey]
MAPPING = [
    (r"(?:Naciones Unidas \(2024\))|(?:\(Naciones Unidas, 2024\))", "[@un2024world]"),
    (r"(?:INE y Sermig \(2023\))|(?:\(INE y Sermig, 2023\))", "[@INE_SERMIG_2023]"),
    (r"(?:Diminescu \(2008\))|(?:\(Diminescu, 2008\))", "[@diminescu2008]"),
    (r"(?:DataReportal \(2024\))|(?:\(DataReportal, 2024\))", "[@DataReportal2024Chile]"),
    (r"(?:Baldassar \(2016\))|(?:\(Baldassar, 2016\))", "[@baldassar2016]"),
    (r"(?:Peñaranda \(2010\))|(?:\(Peñaranda, 2010\))", "[@penaranda2010te]"),
    (r"(?:Peñaranda et al\. \(2011\))|(?:\(Peñaranda et al\., 2011\))", "[@peñaranda2011]"),
    (r"(?:van Dijck \(2013\))|(?:\(van Dijck, 2013\))", "[@vandijck2013]"),
    (r"(?:Zuckerberg \(2006\))|(?:\(Zuckerberg, 2006\))", "[@zuckerberg2006calm]"),
    (r"(?:Zuckerberg \(2008\))|(?:\(Zuckerberg, 2008\))", "[@zuckerberg2008thoughts]"),
    (r"(?:Zuckerberg \(2017\))|(?:\(Zuckerberg, 2017\))", "[@zuckerberg2017manifesto]"),
    (r"(?:WhatsApp \(2024\))|(?:\(WhatsApp, 2024\))", "[@whatsapp2024about]"),
    (r"(?:TikTok \(2024\))|(?:\(TikTok, 2024\))", "[@tiktok_about_2024]"),
    (r"(?:Statista \(2023\))|(?:\(Statista, 2023\))", "[@statista2023chile]"),
    (r"(?:Vertovec \(2009\))|(?:\(Vertovec, 2009\))", "[@vertovec2009transnationalism]"),
    (r"(?:Bailey \(2007\))|(?:\(Bailey, 2007\))", "[@bailey2007transnational]"),
    (r"(?:Bell y Erdal \(2015\))|(?:\(Bell y Erdal, 2015\))", "[@bellerdal2015]"),
    (r"(?:Vermot \(2015\))|(?:\(Vermot, 2015\))", "[@vermot2015]"),
    (r"(?:Nedelcu y Wyss \(2016\))|(?:\(Nedelcu y Wyss, 2016\))", "[@nedelcu2016]"),
    (r"(?:Massey y España \(1987\))|(?:\(Massey y España, 1987\))", "[@massey1987]"),
    (r"(?:Dekker et al\. \(2018\))|(?:\(Dekker et al\., 2018\))", "[@dekker2018smart]"),
    (r"(?:Haythornthwaite \(2002\))|(?:\(Haythornthwaite, 2002\))", "[@haythornthwaite2002strong]"),
    (r"(?:Jayadeva \(2020\))|(?:\(Jayadeva, 2020\))", "[@jayadeva2020]"),
    (r"(?:Hernández Sampieri y Mendoza Torres \(2018\))|(?:\(Hernández Sampieri y Mendoza Torres, 2018\))", "[@hernandezsampieri2018]"),
    (r"(?:Madianou \(2016\))|(?:\(Madianou, 2016\))", "[@madianou2016]"),
    (r"(?:Madianou \(2014\))|(?:\(Madianou, 2014\))", "[@madianou2012]"),
    (r"(?:Pearce y Rice \(2013\))|(?:\(Pearce y Rice, 2013\))", "[@pearce2013digital]"),
    (r"(?:Dedecek Gertz y Süßer \(2022\))|(?:\(Dedecek Gertz y Süßer, 2022\))", "[@dedecek_gertz_migration_2022]"),
    (r"(?:Marat y Zabyelina \(2021\))|(?:\(Marat y Zabyelina, 2021\))", "[@MaratZabyelina2021]"),
    (r"(?:Katz y González \(2016\))|(?:\(Katz y González, 2016\))", "[@gonzalezkatz2016]"),
    (r"(?:Francisco \(2015\))|(?:\(Francisco, 2015\))", "[@bailey2007transnational]"),
    (r"(?:Ryan et al\. \(2009\))|(?:\(Ryan et al\., 2009\))", "[@ryan2009how]"),
]

def update_citations():
    sections_dir = Path("paper/sections")
    for section_file in sections_dir.glob("*.md"):
        content = section_file.read_text(encoding='utf-8')
        new_content = content
        for pattern, replacement in MAPPING:
            new_content = re.sub(pattern, replacement, new_content)
        
        if new_content != content:
            section_file.write_text(new_content, encoding='utf-8')
            print(f"Updated {section_file.name}")

if __name__ == "__main__":
    update_citations()
