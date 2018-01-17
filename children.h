#ifndef CHILD_H
#define CHILD_H

#include <QMap>
#include <QPair>

class Children : public QMap<unsigned int, QPair<unsigned int, unsigned int> >
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
