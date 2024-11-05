"""
CQS (Command Query Separation) and CQRS (Command Query Responsibility Segregation) are very much related.
You can think of CQS as being at the class or component level, while CQRS is more at the bounded context level.

I tend to think of CQS as being at the micro level, and CQRS at the macro level.

CQS prescribes separate methods for querying from or writing to a model: the query doesn't mutate state,
while the command mutates state but does not have a return value. It was devised by Bertrand Meyer as part of his
pioneering work on the Eiffel programming language.

CQRS prescribes a similar approach, except it's more of a path through your system. A query request takes a separate
path from a command. The query returns data without altering the underlying system; the command alters the system
but does not return data.
"""
