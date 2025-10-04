import language_tool_python

def check_paragraph(text):
    # Load English tool (you can change language to "hi" for Hindi, etc.)
    tool = language_tool_python.LanguageTool('en-US')
    
    # Find matches (errors) in text
    matches = tool.check(text)

    if not matches:
        print("✅ No errors found!")
        return

    print(f"⚠️ Found {len(matches)} issues:\n")
    for i, match in enumerate(matches, 1):
        print(f"{i}. {match.ruleId} - {match.message}")
        print(f"   ➤ Error in: '{text[match.offset:match.offset+match.errorLength]}'")
        if match.replacements:
            print(f"   💡 Suggestion(s): {', '.join(match.replacements[:3])}")
        print()

    # Optionally: auto-correct
    corrected = language_tool_python.utils.correct(text, matches)
    print("✅ Corrected version:\n", corrected)

if __name__ == "__main__":
    paragraph = """This is an exmple of a paragraf with some erors. 
    It have many mistake like grammar, spellings and wrong tense used."""
    
    check_paragraph(paragraph)
