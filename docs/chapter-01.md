# Chapter 1: The way of the program
(Watch a video based on this chapter [here on YouTube](https://youtu.be/lhtUREG6vAg).)

# 第一章：编程之道

The goal of this book is to teach you to think like a computer scientist. This way of thinking combines some of the best features of mathematics, engineering, and natural science. Like mathematicians, computer scientists use formal languages to denote ideas (specifically computations). Like engineers, they design things, assembling components into systems and evaluating tradeoffs among alternatives. Like scientists, they observe the behavior of complex systems, form hypotheses, and test predictions.

本书的目标是教你像一名计算机科学家一样思考。这种思考方法结合了数学、工程学和自然科学中一些很好的特点。对数学家、计算机科学家来说，他们使用形式化语言来表示想法（尤其是计算过程）；对于工程师们，他们设计、组装成为系统并在各种方案中进行评估权衡；而对于科学家们而言，他们理解众多复杂系统的步骤，通常是：观察、猜想、验证。

---

The single most important skill for a computer scientist is **problem solving**. Problem solving means the ability to formulate problems, think creatively about solutions, and express a solution clearly and accurately. As it turns out, the process of learning to program is an excellent opportunity to practice problem-solving skills. That’s why this chapter is called, The way of the program.

对一位计算机科学家来说，首要技能是**解决问题**。解决问题体现了表述问题的能力，即有创造性地思考一些解决方案，然后把思考过程清晰准确地表达出来。结果证明，学习编程的过程是一个锻炼解决问题这一技能的绝佳机会。这也正是本章为「编程之道」的原因。

---

On one level, you will be learning to program, a useful skill by itself. On another level, you will use programming as a means to an end. As we go along, that end will become clearer.

在一个层面上，你将会学习如何编程，这个本身就很有用的技能。在另一层面，你将会使用编程作为一种到达终点的方法。当我们继续深入学习，那个终点就会逐渐变得清晰。

---

## 1.1. The Python programming language
## 1.1. Python 编程语言

The programming language you will be learning is Python. Python is an example of a high-level language; other **high-level languages** you might have heard of are C++, PHP, Pascal, C#, and Java.

你将要学习的编程语言叫做 Python，这是一门「高级编程语言」。其它你可能听说过的**高级编程语言** 包括 C++、 PHP、Pascal、C# 和 Java。

---

As you might infer from the name high-level language, there are also **low-level languages**, sometimes referred to as machine languages or assembly languages. Loosely speaking, computers can only execute programs written in low-level languages. Thus, programs written in a high-level language have to be translated into something more suitable before they can run.

正如你可能会从「高级编程语言」这个名字来推理，的确也有一些**低级编程语言**，有时也会被称为「机器语言」或「汇编语言」。宽松地说，计算机只能执行用「低级编程语言」写的程序。换句话说，用「高级编程语言」写的程序，在能运行之前必须要被翻译成一些更适合机器理解的东西，也就是「机器语言」。

---

Almost all programs are written in high-level languages because of their advantages. It is much easier to program in a high-level language so programs take less time to write, they are shorter and easier to read, and they are more likely to be correct. Second, high-level languages are **portable**, meaning that they can run on different kinds of computers with few or no modifications.

因为高级编程语言的优势，几乎所有的程序都是用高级编程语言写的。（相较于机器语言，使用高级编程语言时，）花在写代码上的时间更少，代码更简短且易读，也就更可能写对，因此用高级编程语言编程更容易。其次，高级编程语言都是**可移植的**，意味着写出来的程序只要很少的修改甚至无需修改，就可以在不同种类的计算机上运行。

---

In this edition of the textbook, we use an online programming environment called **Replit**. To follow along with the examples and complete the exercises, all you need is a free account - just navigate to https://replit.com and complete the sign up process.

在这本教材中，我们使用一个叫做 **Replit** 的线上编程环境。你只需要注册一个免费账号，就可以跟着本书的例子学习并完成习题了。访问 https://replit.com 去完成注册吧。

>注: 中文用户推荐使用 [RUNOOB 的在线环境](https://c.runoob.com/compile/9/)，无需注册。本文后续将使用中文在线环境替代 **Replit**。

---

Once you have an account, create a new repl and choose Python as the language from the dropdown. You’ll see it automatically creates a file called `main.py`. By convention, files that contain Python programs have names that end with `.py`.

当你拥有一个账号，新建了一个 repl 并从下拉菜单中选择了 Python 作为编程语言，你将会看到系统自动创建了一个 `main.py` 文件。我们约定，包含 Python 程序的文件以 `.py` 作为文件的扩展名。

> 注：中文用户可以不注册账号，直接在 [RUNOOB 的在线环境](https://c.runoob.com/compile/9/) 中查看，这里系统自动创建的文件名为 `script.py`。

---

The engine that translates and runs Python is called the **Python Interpreter**: There are two ways to use it: immediate mode and script mode. In immediate mode, you type Python expressions into the Python Interpreter window, and the interpreter immediately shows the result:

翻译并运行 Python 的引擎，我们称之为 **Python 解释器**。有两种方式使用 Python 解释器，「即时模式」和「脚本模式」。在「即时模式」，你在 Python 解释器窗口里输入 Python 表达式，然后解释器就会立即显示结果。

---

<!-- ![Running code in the interpreter (immediate mode)](../images/01-01-python-interpreter.png) -->

The `>>>` or `>` is called the **Python prompt**. The interpreter uses the prompt to indicate that it is ready for instructions. We typed `2 + 2`, and the interpreter evaluated our expression, and replied `4`, and on the next line it gave a new prompt, indicating that it is ready for more input.

符号 `>>>` 或 `>` 被称之为 **Python 提示符**。解释器用提示符来表明它已准备好接收指令。我们输入 `2 + 2`，接着解释器就计算我们的这个表达式，然后回复我们 `4`，在下一行，它又给了我们一个新的提示符，表明它正准备接收更多的输入指令。

---

Working directly in the interpreter is convenient for testing short bits of code because you get immediate feedback. Think of it as scratch paper used to help you work out problems. Anything longer than a few lines should be put into a script. Scripts have the advantage that they can be saved to disk, printed, and so on. To create a script, you can enter the code into the middle pane, as shown below

因为你能直接收到反馈，所以使用解释器对于测试一些简短的代码片段来说会很方便。就像用草稿纸来演算一样。但代码量大一点的话，就应该使用脚本了。脚本的优势在于它们更易于被保存到磁盘上、易于打印等等。创建一个脚本，只需要像下面这样把代码输入进文本中即可。

---

<!-- ![Running code from a file (script mode)](../images/01-02-running-a-script.png) -->

```python
print("My first program adds two numbers")
print(2+3)
```

To execute the program, click the **Run** button in Replit. You’re now a computer programmer! Let’s take a look at some more theory before we start writing more advanced programs.

要想执行程序，在网页上点击运行即可。你现在就是一名程序员了！在我们开始写更多高级程序之前，让我们一起先了解一些理论吧。

---

## 1.2. What is a program?
## 1.2. 什么是程序？

A **program** is a sequence of instructions that specifies how to perform a computation. The computation might be something mathematical, such as solving a system of equations or finding the roots of a polynomial, but it can also be a symbolic computation, such as searching and replacing text in a document or (strangely enough) compiling a program.

**程序** 是一个具体说明如何运行一个计算过程的指令序列。计算可以是数学上的，比如解方程或找出一个多项式的根，但也可以是一种形式上的计算，比如在一个文档里查找、替换指定文本，或者干脆就是编译一个程序。

---

The details look different in different languages, but a few basic instructions appear in just about every language:

不同编程语言的细节看起来会不一样，但有一些基本的共通之处：

---

**input**
- Get data from the keyboard, a file, or some other device.

**输入**
- 从键盘、文件或一些设备（如触摸屏）获取数据。

---

**output**
- Display data on the screen or send data to a file or other device.

**输出**
- 在屏幕上展示数据或者把数据传输到一个文件或其它设备。

---

**math**
- Perform basic mathematical operations like addition and multiplication.

**计算**
- 运行诸如加法、乘法的基本数学操作。

---

**conditional execution**
- Check for certain conditions and execute the appropriate sequence of statements.

**条件执行**
- 检查到当满足特定条件时执行合适的表达式序列。

---

**repetition**
- Perform some action repeatedly, usually with some variation.

**循环**
- 重复运行一些动作，通常伴随一些变化。

---

Believe it or not, that’s pretty much all there is to it. Every program you’ve ever used, no matter how complicated, is made up of instructions that look more or less like these. Thus, we can describe programming as the process of breaking a large, complex task into smaller and smaller subtasks until the subtasks are simple enough to be performed with sequences of these basic instructions.

信不信由你，这差不多就是编程的全部了。你曾经使用过的每一个程序，无论多么复杂，都或多或少是这些指令组合而成。因此，我们可以这样描述：编程就是把一个大的、复杂的任务，不断地拆分、拆分、拆分，直到拆分成一系列我们能够以基础指令运行的子任务。

---

That may be a little vague, but we will come back to this topic later when we talk about **algorithms**.

这么说可能有点含糊，等以后讲到**算法**时我们将会再回来讨论这个话题。

---

## 1.3. What is debugging?
## 1.3. 什么是调试？

Programming is a complex process, and because it is done by human beings, it often leads to errors. Programming errors are called **bugs** and the process of tracking them down and correcting them is called **debugging**. Use of the term bug to describe small engineering difficulties dates back to at least 1889, when Thomas Edison had a bug with his phonograph.

编程是一个复杂的过程，因为这是由人来完成的，所以也就导致经常出错。编程中出现的错误被叫做**bug**，追踪并纠正错误的过程就叫**调试（debug）**。我们用 **bug** 这个术语描述工程上遇到的小困难，这个说法至少可以追溯到 1889 年，因为当年托马斯・爱迪生在他的留声机里发现了一只虫子。

---

Three kinds of errors can occur in a program: [syntax errors](https://en.wikipedia.org/wiki/Syntax_error), [runtime errors](https://en.wikipedia.org/wiki/Runtime_(program_lifecycle_phase)), and [semantic errors](https://en.wikipedia.org/wiki/Logic_error). It is useful to distinguish between them in order to track them down more quickly.

在一个程序里可能有三类错误：**语法错误**、**运行时错误**、**语义错误**。为了能够快速追踪定位问题，我们有必要对这三类错误加以区分。

---

## 1.4. Syntax errors
## 1.4. 语法错误

Python can only execute a program if the program is syntactically correct; otherwise, the process fails and returns an error message. **Syntax** refers to the structure of a program and the rules about that structure. For example, in English, a sentence must begin with a capital letter and end with a period. this sentence contains a **syntax error**. So does this one

Python 只有在语法正确时才会执行，不然就会失败并返回错误信息。**语法** 指的是一个程序的结构和结构对应的规则。举个例子，在（书面）英语里，一句话必须以一个大写字母开头、以一个句号结尾。否则，我们就称之为**语法错误**。

---

For most readers, a few syntax errors are not a significant problem, which is why we can read the poetry of E. E. Cummings without problems. Python is not so forgiving. If there is a single syntax error anywhere in your program, Python will display an error message and quit, and you will not be able to run your program. During the first few weeks of your programming career, you will probably spend a lot of time tracking down syntax errors. As you gain experience, though, you will make fewer errors and find them faster.

对于大多数读者来说，有一些语法错误并不是什么严重的问题，这就解释了我们能够毫无障碍地阅读 E. E. Cummings 的诗歌的原因。Python 却不会这么善解人意，在程序里即使只要有一处小小的语法错误，它也会输出错误信息，然后退出。你没办法运行它。在你编程生涯的开头几个星期，你可能会花很多时间面对语法错误。当你有了一些经验之后，你就会少犯错这些语法错误，即使犯了语法错误也能更快地找出来了。

---

## 1.5. Runtime errors
## 1.5. 运行时错误

The second type of error is a runtime error, so called because the error does not appear until you run the program. These errors are also called **exceptions** because they usually indicate that something exceptional (and bad) has happened.

第二类错误叫做「运行时错误」，因这类错误只会发生在运行程序的时而得名。这些错误也叫**异常**，因为它们通常表示一些意想不到的（坏）事发生了。

---

Runtime errors are rare in the simple programs you will see in the first few chapters, so it might be a while before you encounter one.

你将会在开始的几章中发现，运行时错误少见于一些简单的程序中。所以你可能会等一段时间才会遇到这种情况。

---

## 1.6. Semantic errors
## 1.6. 语义错误

The third type of error is the **semantic error**. If there is a semantic error in your program, it will run successfully, in the sense that the computer will not generate any error messages, but it will not do the right thing. It will do something else. Specifically, it will do what you told it to do.

第三类错误叫做**语义错误**。如果你的程序里有一处语义错误，它可能运行成功，也就是说，计算机并不会生成任何错误信息，但是它就是没有做正确的事。它会做一些别的事，不过，它做的完全就是你让它做的。

---

The problem is that the program you wrote is not the program you wanted to write. The meaning of the program (its semantics) is wrong. Identifying semantic errors can be tricky because it requires you to work backward by looking at the output of the program and trying to figure out what it is doing.

问题在于：你写的这个程序做的事，不是你真正想要的。这个程序的想法（语义）是错误的。识别语义错误会很棘手，因为它需要你回过头来从程序的输出结果反推，再尝试理解程序在做什么。

---

## 1.7. Experimental debugging
## 1.7. 试验调试

One of the most important skills you will acquire is debugging. Although it can be frustrating, debugging is one of the most intellectually rich, challenging, and interesting parts of programming.

你将要习得的最重要的技能之一就是调试。尽管有时候会很令人沮丧，调试却是最具智慧、最具挑战的一项技能，也是编程中极有趣的部分。

---

In some ways, debugging is like detective work. You are confronted with clues, and you have to infer the processes and events that led to the results you see.

从某种程度上说，调试就像一份侦探工作。你面对的是各种蛛丝马迹，你必须推理其中的过程，拨开云雾见日明。

---

Debugging is also like an experimental science. Once you have an idea what is going wrong, you modify your program and try again. If your hypothesis was correct, then you can predict the result of the modification, and you take a step closer to a working program. If your hypothesis was wrong, you have to come up with a new one. As Sherlock Holmes pointed out, When you have eliminated the impossible, whatever remains, however improbable, must be the truth. (A. Conan Doyle, _The Sign of Four_)

调试也像是一门试验科学。一旦你知道了问题根源，修改你的程序，然后重试。如果你的猜想是对的，那你在修改的过程中就能预测出结果，然后你离一个正常运行的程序就更近了一步。如果你的猜想不对，那就重新思考。就像福尔摩斯指出的那样，当你排除了不可能的，不管多么不可思议，剩下的都是真相。（A. 柯南・道尔，_四个标记_）

---

For some people, programming and debugging are the same thing. That is, programming is the process of gradually debugging a program until it does what you want. The idea is that you should start with a program that does something and make small modifications, debugging them as you go, so that you always have a working program.

对于一些人来说，编程和调试其实是一回事。那就是说，在你最终完成之前，编程是一个不断调试的过程。一个重要的思想是，你应该从一个可用的小的程序开始，一点一点，不断地修改、调试，这样你就总能保证程序是可用的。

---

For example, Linux is an operating system kernel that contains millions of lines of code, but it started out as a simple program Linus Torvalds used to explore the Intel 80386 chip. According to Larry Greenfield, one of Linus’s earlier projects was a program that would switch between displaying AAAA and BBBB. This later evolved to Linux (_The Linux Users’ Guide_ Beta Version 1).

举例来说，Linux 是一个有着数百万行代码的操作系统内核，但它是从 Linus Torvalds 用来探索英特尔 80836 芯片而写的小程序开始的。据 Larry Greenfield 说，Linus 的早期项目里，有一个小程序，它的作用仅仅是交替打印 AAAA 和 BBBB。但是这个小程序，演进成了后来的 Linux（_Linux 用户指南_ Beta 版本1）。

---

Later chapters will make more suggestions about debugging and other programming practices.

后面的章节，我们会对调试和其它编程实践给出更多的建议。

---

## 1.8. Formal and natural languages
## 1.8. 形式化语言和自然语言

**Natural languages** are the languages that people speak, such as English, Spanish, and French. They were not designed by people (although people try to impose some order on them); they evolved naturally.

**自然语言**是人类讲的语言，如英语、西班牙语、法语。这些不是人类设计的（虽然人类也尝试在里面强加一些规则），而是自然地演进而来。

---

**Formal languages** are languages that are designed by people for specific applications. For example, the notation that mathematicians use is a formal language that is particularly good at denoting relationships among numbers and symbols. Chemists use a formal language to represent the chemical structure of molecules. And most importantly:

**形式化语言**是由人类为特定的应用而设计的语言。举例来说，数学上使用的记号就是一种形式化语言，它能很好地表示数字和符号的关系。化学家使用一种形式化语言来代表分子的化学结构。最重要的是：

---

_Programming languages are formal languages that have been designed to express computations._

_编程语言是被设计为表示计算过程的形式化语言。_

---

Formal languages tend to have strict rules about syntax. For example, `3+3=6` is a syntactically correct mathematical statement, but `3=+6$` is not. `H2O` is a syntactically correct chemical name, but `2Zz` is not.

形式化语言一般都有严格的语法。比如，`3+3=6` 是一个语法上正确的数学语句，但 `3=+6$` 却不是；`H2O` 是一个语法上正确的化学名称，但是 `2Zz` 却不是。

---

Syntax rules come in two flavors, pertaining to **tokens** and structure. Tokens are the basic elements of the language, such as words, numbers, parentheses, commas, and so on. In Python, a statement like `print("Happy New Year for ",2013)` has 6 tokens: a function name, an open parenthesis (round bracket), a string, a comma, a number, and a close parenthesis.

It is possible to make errors in the way one constructs tokens. One of the problems with `3=+6$` is that `$` is not a legal token in mathematics (at least as far as we know). Similarly, `2Zz` is not a legal token in chemistry notation because there is no element with the abbreviation `Zz`.

The second type of syntax rule pertains to the **structure** of a statement— that is, the way the tokens are arranged. The statement `3=+6$` is structurally illegal because you can’t place a plus sign immediately after an equal sign. Similarly, molecular formulas have to have subscripts after the element name, not before. And in our Python example, if we omitted the comma, or if we changed the two parentheses around to say `print)"Happy New Year for ",2013(` our statement would still have six legal and valid tokens, but the structure is illegal.

When you read a sentence in English or a statement in a formal language, you have to figure out what the structure of the sentence is (although in a natural language you do this subconsciously). This process is called **parsing**.

For example, when you hear the sentence, “The other shoe fell”, you understand that the other shoe is the subject and fell is the verb. Once you have parsed a sentence, you can figure out what it means, or the **semantics** of the sentence. Assuming that you know what a shoe is and what it means to fall, you will understand the general implication of this sentence.

Although formal and natural languages have many features in common — tokens, structure, syntax, and semantics — there are many differences:

**ambiguity**
- Natural languages are full of ambiguity, which people deal with by using contextual clues and other information. Formal languages are designed to be nearly or completely unambiguous, which means that any statement has exactly one meaning, regardless of context.

**redundancy**
- In order to make up for ambiguity and reduce misunderstandings, natural languages employ lots of redundancy. As a result, they are often verbose. Formal languages are less redundant and more concise.

**literalness**
- Formal languages mean exactly what they say. On the other hand, natural languages are full of idiom and metaphor. If someone says, “The other shoe fell”, there is probably no shoe and nothing falling. You’ll need to find the original joke to understand the idiomatic meaning of the other shoe falling. Yahoo! Answers thinks it knows!

People who grow up speaking a natural language—everyone—often have a hard time adjusting to formal languages. In some ways, the difference between formal and natural language is like the difference between poetry and prose, but more so:

**poetry**
- Words are used for their sounds as well as for their meaning, and the whole poem together creates an effect or emotional response. Ambiguity is not only common but often deliberate.

**prose**
- The literal meaning of words is more important, and the structure contributes more meaning. Prose is more amenable to analysis than poetry but still often ambiguous.

**program**
- The meaning of a computer program is unambiguous and literal, and can be understood entirely by analysis of the tokens and structure.

Here are some suggestions for reading programs (and other formal languages). First, remember that formal languages are much more dense than natural languages, so it takes longer to read them. Also, the structure is very important, so it is usually not a good idea to read from top to bottom, left to right. Instead, learn to parse the program in your head, identifying the tokens and interpreting the structure. Finally, the details matter. Little things like spelling errors and bad punctuation, which you can get away with in natural languages, can make a big difference in a formal language.

## 1.9. The first program
## 1.9. 第一个程序

Traditionally, the first program written in a new language is called Hello, World! because all it does is display the words, Hello, World! In Python, the script looks like this: (For scripts, we’ll show line numbers to the left of the Python statements.)

按照传统，使用新语言写的第一个程序叫 `Hello World!`。因为它所做的事就是打印出一行 `Hello World!`。在 Python 里，这个脚本看起来就像下面这样（至于脚本，我们会在 Python 的语句的左边显示出行数）：

```python
print("Hello, World!")
```

This is an example of using the print function, which doesn’t actually print anything on paper. It 
displays a value on the screen. In this case, the result shown is

这就是一个使用了打印的函数的例子，它并不真的在纸上打印任何东西。它只是在屏幕上显示一个值。这个例子里，结果看上去就是

```
Hello, World!
```

The quotation marks in the program mark the beginning and end of the value; they don’t appear in the result.

程序里的引号标记着这个值的开始和结束，引号不会显示在结果里。

---

Some people judge the quality of a programming language by the simplicity of the Hello, World! program. By this standard, Python does about as well as possible.

有些人以 Hello World! 这个程序的简洁性来判断一门编程语言的质量。从这个标准来说，Python 做得还不错。

---

## 1.10. Comments
## 1.10. 注释

As programs get bigger and more complicated, they get more difficult to read. Formal languages are dense, and it is often difficult to look at a piece of code and figure out what it is doing, or why.

当程序变得越来越大、越来越复杂的时候，也就越来越难以阅读。形式化语言都很紧凑，也就很难从一些代码片段来分辨出它在做什么，或者为什么这么做。

---

For this reason, it is a good idea to add notes to your programs to explain in natural language what the program is doing.

因为这个原因，给你的程序添加注解，用自然语言对程序在做什么进行解释，就是一个好主意了。

---

A **comment** in a computer program is text that is intended only for the human reader — it is completely ignored by the interpreter.

在一个计算机程序里，一个**注释**就是一段给人类阅读的文本 ———— 解释器会完全无视它。

---

In Python, the `#` token starts a comment. The rest of the line is ignored. Here is a new version of Hello, World!.

在 Python 里，`#` 记号标志着注释的开始。那一行余下的部分会被忽略。下面看一个新版本的 Hello World！ 程序。

---

```python
#---------------------------------------------------
# This demo program shows off how elegant Python is!
# Written by Joe Soap, December 2010.
# Anyone may freely copy or modify this program.
#---------------------------------------------------

print("Hello, World!")     # Isn't this easy!
```

You’ll also notice that we’ve left a blank line in the program. Blank lines are also ignored by the interpreter, but comments and blank lines can make your programs much easier for humans to parse. Use them liberally!

你也一定注意到了我们在上面的程序里留了一处空行。空行也会被解释器忽略，但注释和空行能让你的程序更适合人类解析。好好使用它们！

---

## 1.11. Glossary
## 1.11. 术语

**algorithm**

A set of specific steps for solving a category of problems.

**算法**

一个用来解决一类问题的明确的步骤的集合

---

**bug**

An error in a program.

**错误**

程序里的错误。

---

**comment**

Information in a program that is meant for other programmers (or anyone reading the source code) and has no effect on the execution of the program.

**注释**

在程序里对程序员（或任何阅读源码的人）有意义，但是不会被执行的一段信息。

---

**debugging**

The process of finding and removing any of the three kinds of programming errors.

**调试**

寻找并移除任何可能的三种程序错误的过程。

---

**exception**

Another name for a runtime error.

**异常**

运行时错误的另一个说法。

---

**formal language**

Any one of the languages that people have designed for specific purposes, such as representing mathematical ideas or computer programs; all programming languages are formal languages.

**形式化语言**

任何一种由人类为明确的目的，比如表示数学思想或计算机程序，而设计的语言。所有的编程语言都是形式化语言。

---

**high-level language**

A programming language like Python that is designed to be easy for humans to read and write.

**高级语言**

一种被设计成易于人类读写的编程语言，比如 Python。

---

**immediate mode**

A style of using Python where we type expressions at the command prompt, and the results are shown immediately. Contrast with script, and see the entry under Python shell.

**即时模式**

一种使用 Python 时，在命令行提示符处输入表达式，立即得到结果反馈的方式。#$@!%
TODO: 这里不太好翻译，以后再来填坑。

---

**interpreter**

The engine that executes your Python scripts or expressions.

**解释器**

执行 Python 脚本或表达式的引擎。

---

**low-level language**

A programming language that is designed to be easy for a computer to execute; also called machine language or assembly language.

**低级语言**

被设计成简易得可供计算机执行的编程语言，也称「机器语言」或「汇编语言」。

---

**natural language**

Any one of the languages that people speak that evolved naturally.

**自然语言**

任何一种经自然演化的人类使用的语言。

---

**object code**

The output of the compiler after it translates the program.

**目标代码**

编译器将程序翻译后的输出结果。

---

**parse**

To examine a program and analyze the syntactic structure.

**解析**

检测程序并分析其语法结构。

---

**portability**

A property of a program that can run on more than one kind of computer.

**可移植性**

程序可以在多种计算机上运行的属性。

---

**print function**

A function used in a program or script that causes the Python interpreter to display a value on its output device.

**打印函数**

一个在程序或脚本中使用的，可以使 Python 解释器在其输出设备上显示结果的函数。

---

**problem solving**

The process of formulating a problem, finding a solution, and expressing the solution.

**求解**

一个形式化问题、寻找答案并表述解决方案的过程。

---

**program**

a sequence of instructions that specifies to a computer actions and computations to be performed.

**程序**

一系列针对计算机动作和指导计算过程的明确的指令。

---

**Python shell**

An interactive user interface to the Python interpreter. The user of a Python shell types commands at the prompt (`>>>`), and presses the return key to send these commands immediately to the interpreter for processing. The word shell comes from Unix. In the PyScripter used in this RLE version of the book, the Interpreter Window is where we’d do the immediate mode interaction.

**Python 控制台**

Python 解释器的一个可交互用户界面。用户在提示符（`>>>`）处输入命令，按下回车键后就立即把命令发往解释器处理。Shell 一词来自 Unix。

---

**runtime error**

An error that does not occur until the program has started to execute but that prevents the program from continuing.

**运行时错误**

只发生在程序开始执行时阻止程序继续运行的一种错误。

---

**script**

A program stored in a file (usually one that will be interpreted).

**脚本**

（通常会被运行的）保存在文件里的程序。

---

**semantic error**

An error in a program that makes it do something other than what the programmer intended.

**语义错误**

一种使程序不按程序员的想法运行的错误。

---

**semantics**

The meaning of a program.

**语义**

程序的含义。

---

**source code**

A program in a high-level language before being compiled.

**源代码**

被编译之前的高级语言程序。

---

**syntax**

The structure of a program.

**语法**

程序的结构。

---

**syntax error**

An error in a program that makes it impossible to parse — and therefore impossible to interpret.

**语法错误**

程序里的无法解析从而无法运行的一种错误。

---

**token**

One of the basic elements of the syntactic structure of a program, analogous to a word in a natural language.

**记号**

程序语法结构中的一个基本元素。类似于自然语言中的一个单词。

---

## 1.12. Exercises
1. Write an English sentence with understandable semantics but incorrect syntax. Write another English sentence which has correct syntax but has semantic errors.

2. Using the Python interpreter, type `1 + 2` and then hit return. Python evaluates this expression, displays the result, and then shows another prompt. `*` is the multiplication operator, and `**` is the exponentiation operator. Experiment by entering different expressions and recording what is displayed by the Python interpreter.

3. Type `1 2` and then hit return. Python tries to evaluate the expression, but it can’t because the expression is not syntactically legal. Instead, it shows the error message:

    ```python
    File "<interactive input>", line 1
        1 2
        ^
    SyntaxError: invalid syntax
    ```

In many cases, Python indicates where the syntax error occurred, but it is not always right, and it doesn’t give you much information about what is wrong.

So, for the most part, the burden is on you to learn the syntax rules.

In this case, Python is complaining because there is no operator between the numbers.

See if you can find a few more examples of things that will produce error messages when you enter them at the Python prompt. Write down what you enter at the prompt and the last line of the error message that Python reports back to you.

4. Type `print("hello")`. Python executes this, which has the effect of printing the letters h-e-l-l-o. Notice that the quotation marks that you used to enclose the string are not part of the output. Now type `"hello"` and describe your result. Make notes of when you see the quotation marks and when you don’t.

5. Type cheese without the quotation marks. The output will look something like this:

    ```python
    Traceback (most recent call last):
    File "<interactive input>", line 1, in ?
    NameError: name 'cheese' is not defined
    ```

This is a run-time error; specifically, it is a NameError, and even more specifically, it is an error because the name cheese is not defined. If you don’t know what that means yet, you will soon.

6. Type `6 + 4 * 9` at the Python prompt and hit enter. Record what happens.

Now create a Python script with the following contents:

```
6 + 4 * 9
```

What happens when you run this script? Now change the script contents to:

```python
print(6 + 4 * 9)
```

and run it again.

What happened this time?

Whenever an expression is typed at the Python prompt, it is evaluated and the result is automatically shown on the line below. (Like on your calculator, if you type this expression you’ll get the result 42.)

A script is different, however. Evaluations of expressions are not automatically displayed, so it is necessary to use the **print** function to make the answer show up.

It is hardly ever necessary to use the print function in immediate mode at the command prompt.
