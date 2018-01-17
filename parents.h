#ifndef PARENT_H
#define PARENT_H

#include <QMap>
#include <QPair>

class Parents : public QMap<unsigned int, QPair<unsigned int, unsigned int> >
{
public:
    Parents()
    {

    }

    virtual ~Parents()
    {
    }
};

#endif // PARENT_H
