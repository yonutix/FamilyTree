#ifndef TREEMANAGER_H
#define TREEMANAGER_H

#include <QVector>
#include "individual.h"
#include "parents.h"
#include "children.h"

class TreeManager
{
public:
    TreeManager()
    {
    }

    ~TreeManager()
    {
    }


    void loadData(QVector<Individual>& individuals, Parents& parents, Children& children, QString const& path)
    {

    }

    void saveData(QVector<Individual>& individuals, Parents& parents, Children& children, QString const& path)
    {

    }
};

#endif // TREEMANAGER_H
