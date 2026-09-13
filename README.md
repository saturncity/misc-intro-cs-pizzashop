> [!WARNING]
> This is a terminal pizza ordering simulator I wrote in November 2020 for an intro computer science class, and I haven't touched the logic since. It runs, but it crashes if you type anything non-numeric at a price prompt, and in one case the itemized cart shows the wrong price next to each topping. I've documented both in [Known issues](#known-issues) rather than fixing them, because the point of keeping this around is the record of what I could write at the time.

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![No dependencies](https://img.shields.io/badge/dependencies-none-6E6E6E?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-3DA639?style=for-the-badge)

</div>

## About

I built this as the Lesson 12 performance task for my intro CS course. You give it your name and a budget, pick toppings off a numbered menu, and it walks you through a fake delivery countdown before handing over the pizza. A plain pizza costs 5 USD, each topping adds to that, and it won't let you add a topping that would put you over the budget you named.

It's one file, one loop, and no imports beyond `time`. It all runs in the terminal: `input()` collects your answers, `print()` redraws the menu and the cart, and `time.sleep()` paces the countdown.

- Numbered topping menu with per-item prices, reprinted in full after every invalid choice
- A budget check before each topping goes in, so the total can't pass what you said you'd spend
- Running cart total that folds in the 5 USD base pizza
- It rejects a menu number outside the list and asks again instead of crashing
- Ten second delivery countdown with stage labels (prep, toppings, baking, boxing, delivery)
- Loops back around to a fresh order once a delivery finishes

## Tech stack

| Layer | Technology | Why it's here |
| --- | --- | --- |
| Language | Python 3.6 or newer | The whole program. It needs 3.6 at minimum for the f-strings it uses on nearly every line. |
| Standard library | `time` | The only import. `time.sleep()` paces the delivery countdown and the pause after an insufficient funds message. |
| Interface | Terminal stdin and stdout | `input()` and `print()`. No GUI, no curses, no color codes. |

## What it looks like

No screenshots, because nothing here renders outside a terminal. Both samples below are real output, captured by piping answers into the program on Python 3.9.6. The only edits are where I trimmed the tail.

A full order, from name to delivery. The countdown lines arrive one per second rather than all at once:

```text
WHAT IS YOUR NAME?

OKAY SAM, HOW MUCH MONEY DO YOU WANT TO SPEND? (USD) [PLAIN PIZZA IS 5 USD]

TOPPINGS

1. NO TOPPINGS - 0 USD
2. EXTRA CHEESE - 1 USD
3. PARM - 1 USD
4. PEPPERONI - 3 USD
5. BACON - 2 USD
6. SAUSAGE - 3 USD

WHAT TOPPING WOULD YOU LIKE TO ADD?
YOU ADDED PEPPERONI FOR 3 USD.

YOUR SHOPPING CART NOW (8 USD TOTAL):

1. PEPPERONI - 3 USD

SAM, ARE YOU FINISHED WITH YOUR ORDER?

TOPPINGS

1. NO TOPPINGS - 0 USD
2. EXTRA CHEESE - 1 USD
3. PARM - 1 USD
4. PEPPERONI - 3 USD
5. BACON - 2 USD
6. SAUSAGE - 3 USD

WHAT TOPPING WOULD YOU LIKE TO ADD?
YOU ADDED BACON FOR 2 USD.

YOUR SHOPPING CART NOW (10 USD TOTAL):

1. PEPPERONI - 3 USD

2. BACON - 2 USD

SAM, ARE YOU FINISHED WITH YOUR ORDER?

SAM, WHERE WOULD YOU LIKE THIS PIZZA SENT TO?

PIZZA ORDERED! IT WILL TAKE ABOUT 10 SECONDS TO DELIVER

10 (PIZZA PREP)
9 (ADDING TOPPINGS)
8
7 (BAKING THE PIZZA)
6
5 (BOXING THE PIZZA)
4 (DELIVERY BEGINS)
3
2
1 (ARRIVED AT 742 EVERGREEN TERRACE)

DELIVERY GUY: HERE YOU GO SAM ENJOY THIS PIZZA WITH ['PEPPERONI', 'BACON']!

(ORDER ANOTHER PIZZA IN 10 SECONDS)
```

An invalid menu number, then a topping the budget won't cover. Note the order of those last three blocks, which is [Known issue 5](#known-issues):

```text
OKAY SAM, HOW MUCH MONEY DO YOU WANT TO SPEND? (USD) [PLAIN PIZZA IS 5 USD]

TOPPINGS

1. NO TOPPINGS - 0 USD
2. EXTRA CHEESE - 1 USD
3. PARM - 1 USD
4. PEPPERONI - 3 USD
5. BACON - 2 USD
6. SAUSAGE - 3 USD

WHAT TOPPING WOULD YOU LIKE TO ADD?

NUMBER 9 IS NOT AN OPTION

1. NO TOPPINGS - 0 USD
2. EXTRA CHEESE - 1 USD
3. PARM - 1 USD
4. PEPPERONI - 3 USD
5. BACON - 2 USD
6. SAUSAGE - 3 USD

WHAT TOPPING WOULD YOU LIKE TO ADD?
YOU ADDED PEPPERONI FOR 3 USD.

INSUFFICIENT FUNDS.

YOUR SHOPPING CART NOW (5 USD TOTAL):

SAM, ARE YOU FINISHED WITH YOUR ORDER?
```

## Getting started

### Prerequisites

- Python 3.6 or newer. Anything older fails on the f-strings, which show up on nearly every line. I last ran it on 3.9.6.
- Nothing else. `time` ships with Python, so there's no `requirements.txt` and no `pip install` step.

### Installation

There's no install step. Clone it:

```bash
git clone https://github.com/saturncity/misc-intro-cs-pizzashop.git
cd misc-intro-cs-pizzashop
```

### Running

```bash
python3 pizzashop.py
```

It takes over the terminal and reads from stdin. It isn't a server, so there's no port and no URL to open. Answer the prompts as they come, and type lowercase `yes` when you're done adding toppings, since that's the only spelling the check accepts. Ctrl+C is how you get out.

## Project structure

```text
.
├── pizzashop.py   # the entire program: 74 lines, top to bottom, no functions
├── LICENSE
└── README.md
```

## Known issues

I found these by reading the code and confirming each one against a real run. I'm leaving all of them alone. It's a finished class assignment, and patching it now would turn it into something I didn't write in 2020.

1. **Cart line items can show the wrong price.** When a topping would put you over budget, the rollback calls `orderedtoppings.remove(...)` and `orderedprices.remove(...)`. `list.remove` deletes the first matching value rather than the item just appended, so the program pulls the wrong price out whenever two toppings cost the same. On a 9 USD budget, add EXTRA CHEESE and PEPPERONI, then try to add PARM: the cart prints `EXTRA CHEESE - 3 USD` and `PEPPERONI - 1 USD`. The total stays right and only the itemized lines are wrong.
2. **It crashes on any non-numeric answer at a price or menu prompt.** `int(input(...))` sits bare in three places with no `try` around it. Type `ten` instead of `10` and you get a `ValueError` traceback and lose the cart.
3. **Only lowercase `yes` finishes an order.** The test is `done == 'yes'`, so type `YES` or `Y` and you land back in the topping menu with nothing to explain why. Every prompt in the program is uppercase, which makes `YES` the natural thing to type.
4. **`NO TOPPINGS` is orderable.** It's option 1 and it appends to the cart like any other topping, so you can stack `1. NO TOPPINGS - 0 USD` and `2. NO TOPPINGS - 0 USD` on one pizza. It should have ended the topping loop instead.
5. **It tells you a topping was added before checking that you can afford it.** `YOU ADDED PEPPERONI FOR 3 USD.` prints first, then the budget check runs, then the rollback quietly takes it back out. On a 6 USD budget you see the confirmation, then `INSUFFICIENT FUNDS.`, then an empty cart, in that order.
6. **The delivery line prints a raw Python list.** You get `ENJOY THIS PIZZA WITH ['PEPPERONI', 'BACON']!`, brackets and quotes and all.
7. **There's no clean exit.** The outer loop is `while 1==1` with no `break` anywhere, so Ctrl+C is the only way out.
8. **The low-budget path asks twice, in two different wordings.** The re-prompt is an `if` rather than a `while`, and it leaves out the `[PLAIN PIZZA IS 5 USD]` hint that the first prompt has. Enter something under 5 twice and the outer loop runs the check again anyway, so this works by accident rather than by design.
9. **You wait 15 seconds of dead terminal between orders.** After the countdown there's a `time.sleep(5)`, a notice, and then a `time.sleep(10)` before it asks your name again. I thought it was funny at the time.

There are no `TODO` or `FIXME` comments in the source, and no comments of any other kind either.

## Contributing

This is a finished school assignment, so I'm not taking changes to it. If you're working through the same course and something in here is useful to you, take it. If I got something wrong in the list above, open an issue and I'll read it.

## License

MIT, see [LICENSE](LICENSE). Take it, change it, use it in your own coursework. Keep the copyright line and don't come to me when the cart prints the wrong price.
