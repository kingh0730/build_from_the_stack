from dataset_apps_decode_gen_input.langchain_dsl.i_love_programming import (
    i_love_programming,
    i_love_programming_template,
    i_love_programming_chain,
)
from dataset_apps_decode_gen_input.langchain_dsl import (
    DSL_PROMPT_1_INTRO,
    QUESTION_2,
    DSL,
)
from dataset_apps_decode_gen_input.langchain_dsl.template import (
    dsl_chain,
    dsl_template,
)


def test_i_love_programming_template():
    ans = i_love_programming_template()
    print(ans)


def test_DSL_PROMPT_1_INTRO():
    print(DSL_PROMPT_1_INTRO)
    assert type(DSL_PROMPT_1_INTRO) == str


def test_DSL():
    print(DSL)
    assert type(DSL) == str


def test_dsl_template():
    ans = dsl_template(question=QUESTION_2)
    print(ans)
    print(ans[0].content)
    print(ans[1].content)
    assert type(ans) == list
    assert type(ans[0].content) == str
    assert type(ans[1].content) == str


# Too expensive
def not_running():
    def test_i_love_programming():
        ans = i_love_programming()
        print(ans)

    def test_i_love_programming_chain():
        ans = i_love_programming_chain()
        print(ans)
        assert type(ans) == str

    def test_dsl_chain():
        ans = dsl_chain(question=QUESTION_2)
        print(ans)
        assert type(ans) == str
