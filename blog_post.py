import sys,os
from datetime import datetime
import subprocess
import errno
from string import punctuation


def template():
    post_template ="""
    ---\ntitle: {title} \ndate: {year}-{month}-{day}\ntags: \nslug: {slug}\ndraft: true\n---
    \n\n\n\n  {{{{% zoom-img src="/images/{slug}/ "%}}}}
    """
    return post_template






def fill_md(md_temp,title,slug):
    today = datetime.today()
    md_file= "content/posts/{}.md".format(slug)
    md_post = md_temp.strip().format(title=title,
                                    year = today.year,
                                    month = '{:02d}'.format(today.month),
                                    day = '{:02d}'.format(today.day), 
                                    slug = slug)
    if not os.path.exists(md_file):
        with open(md_file, 'w') as w:
            w.write(md_post)
        print("{}\tCREATED".format(md_file))
    else:
        print('{}\tEXIST'.format(md_file))


def clean_title(title):
    '''Clean the title'''
    rem_pun = ''.join(c for c in title if c not in punctuation)  # remove punctuations
    clean_title = ' '.join(rem_pun.split())  # remove spaces
    return clean_title

def slug_title(title):
    '''slug the title'''
    slug = title.lower().strip().replace(' ', '-')
    return slug

def make_dirs(slug):
    '''create directories'''
    img_dir = 'content/images/{}'.format(slug)  # images directory
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
        print("{}/\tCREATED".format(img_dir))
    else:
        print("{}/\tEXIST".format(img_dir))


def make_md(slug):
    '''String with location of markdown post '''
    md_post= "content/posts/{}.md".format(slug)
    if not os.path.exists(md_post):  # check if markdown file exist.
        with open(md_post, 'w') as f:  # create an emtpy file
            f.write('')
            # print(type(md_post))
            # print(md_post)
            return md_post
    else:
        print('.md Already Exist')


def dir_test(slug):
    img_dir = 'content/images/{}'.format(slug)  # images directory
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
        print('file created')
    else:
        print('Dir Already Exist')


def main(title):
    """Main entry point for the script."""
    title_clean = clean_title(title)
    md_temp = template()  # load empty template function
    bg_slug = slug_title(title_clean)  # create slug
    make_dirs(bg_slug)  # create image directory
    fill_md(md_temp,title,bg_slug)  # load empty template with data and save




if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].strip() !="" :
        sys.exit(main(sys.argv[1]))
    else:
        print ("Not a valid title")