#ifndef UIMANAGER_H
#define UIMANAGER_H

#include <QDebug>

#include "QObject"
#include "uilistener.h"

class UIManager : public QObject
{
    Q_OBJECT



public:
    UIManager()
    {

    }

    void setListener(UIListener* listener)
    {
        m_uiListener = listener;
    }

    Q_INVOKABLE void requestSubmit(QString const& id, QString const& firstName, QString const& lastName, QString const& sex, QString const& children)
    {

        QList<unsigned int> childrenData;
        QList<QString> childrenRawData = children.split(", ");
        for(int i = 0; i < childrenRawData.size(); ++i)
        {
            childrenData.append((unsigned int)childrenRawData[i].toInt());
        }

        m_uiListener->onNewIndividual(static_cast<unsigned int>(id.toInt()), firstName, lastName.split(" "), sex=="M", childrenData);
    }

    Q_INVOKABLE void requestLoad(QString const& path)
    {
        m_uiListener->onLoadButtonPressed(path);
    }

    Q_INVOKABLE void requestSave(QString const& path)
    {
        m_uiListener->onSaveButtonPressed(path);
    }

private:

    UIListener* m_uiListener;
};

#endif // UIMANAGER_H
