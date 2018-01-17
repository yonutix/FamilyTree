#ifndef FAMILYTREE_H
#define FAMILYTREE_H

#include <QObject>
#include <QVector>
#include <QDebug>

#include "children.h"
#include "parents.h"
#include "individual.h"
#include "uilistener.h"
#include "uimanager.h"

class FamilyTree : public QObject, UIListener
{
    Q_OBJECT
public:
    explicit FamilyTree()
    {
        m_uiManager.setListener(this);
    }

    virtual ~FamilyTree()
    {}

    UIManager* getUIManager() { return &m_uiManager;}

public slots:
    void onNewIndividual(bool value)
    {

    }

private:

    QVector<Individual> m_individuals;

    Children m_children;
    Parents m_parents;

    UIManager m_uiManager;

};

#endif // FAMILYTREE_H
