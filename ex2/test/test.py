from ex2.logic.logic import replace_word


def test_replace_word():
    assert replace_word("I love my cats", "cats", "dog") == ["I love my dog", "cats", "dog", 1]
    assert replace_word("I don't have a car", "a car", "money") == ["I don't have money", "a car", "money", 1]
    assert (replace_word("I will do this, and this and this", "this", "those") ==
            ["I will do those, and those and those", "this", "those", 3])
