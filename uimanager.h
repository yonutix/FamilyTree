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

    Q_INVOKABLE void requestSubmit()
    {
        qDebug()<<"Submit pressed";
    }

private:

    UIListener* m_uiListener;
};

#endif // UIMANAGER_H
