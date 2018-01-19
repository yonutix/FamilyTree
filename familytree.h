#ifndef FAMILYTREE_H
#define FAMILYTREE_H

#include <QObject>
#include <QList>
#include <QDebug>
#include <QFile>
#include <QXmlStreamWriter>

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

    virtual void onSaveButtonPressed(QString const& path)
    {
        QFile file(path.mid(8));
        file.open(QIODevice::WriteOnly);

        QXmlStreamWriter xmlWriter(&file);
        xmlWriter.setAutoFormatting(true);
        xmlWriter.writeStartDocument();

        xmlWriter.writeStartElement("famiyTree");
        xmlWriter.writeStartElement("individuals");

        for(int i = 0; i < m_individuals.size(); ++i)
        {
            xmlWriter.writeStartElement("individual");

            xmlWriter.writeTextElement("ID", QString::number(m_individuals[i].getId()));

            xmlWriter.writeTextElement("firstName", m_individuals[i].getFirstName());

            xmlWriter.writeStartElement("allLastNames");
            for(int j = 0; j < m_individuals[i].getLastName().size(); ++j)
            {
                xmlWriter.writeTextElement("lastName", m_individuals[i].getLastName()[j]);
            }
            xmlWriter.writeEndElement();//allLastNames

            xmlWriter.writeStartElement("sex");
            xmlWriter.writeEndElement();//sex




            xmlWriter.writeEndElement();//individual

        }

        xmlWriter.writeEndElement();//individuals

        xmlWriter.writeEndElement(); //familyTree

        file.close();
    }

    virtual void onLoadButtonPressed(QString const& path)
    {

    }

    virtual void onNewIndividual(unsigned int id, QString const& firstName, QList<QString> lastName, bool sex)
    {
        m_individuals.append(Individual(id, firstName, sex, lastName));
    }

private:

    QList<Individual> m_individuals;

    Children m_children;
    Parents m_parents;

    UIManager m_uiManager;

};

#endif // FAMILYTREE_H
