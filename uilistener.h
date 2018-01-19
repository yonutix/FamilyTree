#ifndef UILISTENER_H
#define UILISTENER_H

#include <QList>

class UIListener
{
public:
    virtual void onSaveButtonPressed(QString const&) = 0;
    virtual void onLoadButtonPressed(QString const&) = 0;
    virtual void onNewIndividual(unsigned int id, QString const& firstName, QList<QString> lastName, bool sex ) = 0;
};

#endif // UILISTENER_H
