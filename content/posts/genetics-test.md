---
{
  "title": "genetics test",
  "subtitle": "Generic subtitle",
  "date": "2018-07-03",
  "slug": "genetics-test"
}
---

whaqt to wriite
<!--more-->

Minim sunt sunt dolore culpa consequat irure non irure id non fugiat. Quis reprehenderit voluptate cupidatat enim dolore deserunt magna nulla pariatur cupidatat anim laboris incididunt. Aute do quis qui et ullamco proident. Incididunt sint aute dolore sint. Mollit et sit ea consectetur incididunt minim culpa consequat ad ullamco culpa voluptate et ut. Labore consectetur commodo tempor aliquip ea anim est labore est qui ut commodo et.

Est aliqua duis tempor excepteur. Esse reprehenderit reprehenderit aliqua aute. Eu esse non voluptate incididunt labore qui amet est id aliquip ea.


```python
#input:  AAAACCCGGT
#output: ACCGGGTTTT
# T -> A, A -> T
# G -> C, C -> G
#code = {'A': 'T','T':'A','C':'G', 'G':'C'}
def reverse_code(text):
    code = {'A': 'T','T':'A','C':'G', 'G':'C'}
    new_text = ''
    rev_t = text[::-1]
    for i in (rev_t):
        if i in code.keys():
            new_text += code.get(i)
        else:
            print('not!')
    return new_text
```

```python
s_in='AAAACCCGGT'
reverse_code(s_in)
```

    'ACCGGGTTTT'


