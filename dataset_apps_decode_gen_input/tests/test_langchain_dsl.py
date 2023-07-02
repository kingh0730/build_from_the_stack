from dataset_apps_decode_gen_input.langchain_dsl.i_love_programming import (
    i_love_programming,
    i_love_programming_template,
    i_love_programming_chain,
)

from dataset_apps_decode_gen_input.langchain_dsl import (
    DSL_PROMPT_1_INTRO,
)


def test_i_love_programming():
    ans = i_love_programming()
    print(ans)


def test_i_love_programming_template():
    ans = i_love_programming_template()
    print(ans)


def test_i_love_programming_chain():
    ans = i_love_programming_chain()
    print(ans)
    assert type(ans) == str


def test_DSL_PROMPT_1_INTRO():
    print(DSL_PROMPT_1_INTRO)
    assert type(DSL_PROMPT_1_INTRO) == str
