from aiogram.dispatcher.filters.state import StatesGroup, State


class MenuStates(StatesGroup):
    what_do_you_want       = State()
    go_to_manager          = State()
    ask_question           = State()
    state_navigator        = State()
    questons               = State()

    prise                  = State()
    delivering             = State()
    payment                = State()

    go_back                = State()

