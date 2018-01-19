#ifndef CHILD_H
#define CHILD_H

#include <QMap>
#include <QSet>

class Children : public QMap<unsigned int, QSet<unsigned int> >
{
public:
    Children()
    {
    }

    virtual ~Children()
    {

    }
};

#endif // CHILD_H
