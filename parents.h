#ifndef PARENT_H
#define PARENT_H

#include <QMap>
#include <QSet>

class Parents : public QMap<unsigned int, QSet<unsigned int> >
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
