#ifndef INDIVIDUAL_H
#define INDIVIDUAL_H

#include <QList>
#include <QDate>

class Individual
{
public:
    Individual(unsigned int id, QString firstName, bool sex, QList<QString> lastName = {}, QDate birthday = QDate(), QDate deathday = QDate())
    {
        m_id = id;
        m_firstName = firstName;
        m_sex = sex;
        m_lastName = lastName;
        m_birthday = birthday;
        m_deathday = deathday;

    }

    ~Individual()
    {
    }

    unsigned int getId() const { return m_id;}
    QString getFirstName() const { return m_firstName;}
    bool getSex() const { return m_sex;}
    QList<QString> getLastName() const { return m_lastName;}
    QDate getBirthday() const { return m_birthday;}
    QDate getDeathday() const { return m_deathday;}

    void setId(unsigned int id) {m_id = id;}
    void setFirstName(QString& firstName) {m_firstName = firstName;}
    void setSex(bool sex) {m_sex = sex;}
    void setLastName(QList<QString>& lastName) {m_lastName = lastName;}
    void setBirthday(QDate& birthday) {m_birthday = birthday;}
    void setDeathday(QDate& deathday) {m_deathday = deathday;}

    static const Individual UNKNOWN_INDIVIDUAL;


private:
    unsigned int m_id;
    QString m_firstName;
    bool m_sex;

    QList<QString> m_lastName;
    QDate m_birthday;
    QDate m_deathday;

};

#endif // INDIVIDUAL_H
