from lxml import html

# Read the HTML file
with open("/home/k/kit/amat_study_aast/amat_study/amat_question_prepare.html", "r", encoding="utf-8") as f:
    content = f.read()

# Parse the HTML
tree = html.fromstring(content)

question_number = 159
# Iterate over all question divs
questions = tree.xpath('//*[contains(@class, "question")]')
print(len(questions))
for div in questions:
    # Extract the base number from the div id
    # old_div_id = div.get("id")
    # _number = str(old_div_id.split("_")[-1])
    # new_number = '{}'.format(question_number)
    # div_id = 'question_ps_important_{}'.format(question_number)
    # div.set("id", div_id)

    # Update all child elements with ids containing the same number
    # for elem in div.xpath(".//*[@id]"):
    #     elem_id = elem.get("id")
    #     if _number in elem_id:
    #         elem.set("id", elem_id.replace(_number, str(new_number)))

    # # Update 'for' attributes in labels if they reference the old id
    # for label in div.xpath(".//label[@for]"):
    #     label_for = label.get("for")
    #     if _number in label_for:
    #         label.set("for", label_for.replace(_number, str(new_number)))

    # for inp in div.xpath(".//input[@name]"):
    #     inp_name = inp.get("name")
    #     if _number in inp_name:
    #         inp.set("name", inp_name.replace(_number, str(new_number)))

    for elm in div.xpath('.//h3'):
        additional_content = '{}- '.format(question_number)
        elm.text =  '{}{}'.format(additional_content, elm.text)

    
    question_number += 1

# Convert back to string
new_html = html.tostring(tree, pretty_print=True, encoding="unicode")

# Save the modified HTML
with open("/home/k/kit/amat_study_aast/amat_study/amat_question_prepare.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("Updated HTML saved to questions_updated.html")
print(question_number)