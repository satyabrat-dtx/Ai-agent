# DB2ADMIN.WRKEMPLOYEEREPORT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 162
- **Primary key**: `CREATIONTIMESTAMP`, `CREATIONUSER`, `COMPANYCODE`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 170658

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) | NOT NULL | PK | primary_key audit | User who created the row (audit). |
| 2 | `COMPANYCODE` | CHAR(20) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `COMPANYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 4 | `EMPLOYEECODE` | CHAR(20) |  |  |  |  |
| 5 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `CATEGORYCODE` | CHAR(10) |  |  |  |  |
| 7 | `CATEGORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 8 | `SUBCATEGORYCODE` | CHAR(10) |  |  |  |  |
| 9 | `SUBCATEGORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 10 | `WRKDAILYATTENDANCE` | VARCHAR(80) |  |  |  |  |
| 11 | `DIVISIONCODE` | CHAR(10) |  |  |  | Division within a company; second-level organisational discriminator. |
| 12 | `DIVISIONDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 13 | `FACTORYCODE` | CHAR(10) |  |  |  |  |
| 14 | `FACTORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 15 | `DEPARTMENTCODE` | CHAR(10) |  |  |  |  |
| 16 | `DEPARTMENTDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 17 | `SECTIONCODE` | CHAR(10) |  |  |  |  |
| 18 | `SECTIONDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 19 | `MACHINETYPECODE` | CHAR(10) |  |  |  |  |
| 20 | `MACHINEDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 21 | `GRADE` | CHAR(10) |  |  |  |  |
| 22 | `EMPLOYEENAME` | CHAR(100) |  |  |  |  |
| 23 | `DESIGNATION` | CHAR(10) |  |  |  |  |
| 24 | `DESIGNATIONDESC` | VARCHAR(200) |  |  |  |  |
| 25 | `GRADEDESC` | VARCHAR(200) |  |  |  |  |
| 26 | `DATEOFJOINING` | DATE |  |  |  |  |
| 27 | `ESINO` | CHAR(20) |  |  |  |  |
| 28 | `PFNO` | CHAR(20) |  |  |  |  |
| 29 | `TOTALPAYABLEDAYS` | DECIMAL(3,0) |  |  |  |  |
| 30 | `TOTALABSENT` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 31 | `TOTALWEEKOFF` | DECIMAL(3,0) |  |  |  |  |
| 32 | `TOTALHOLIDAY` | DECIMAL(3,0) |  |  |  |  |
| 33 | `TOTALLEAVE` | DECIMAL(3,0) |  |  |  |  |
| 34 | `TOTALPRESENT` | DECIMAL(3,0) |  |  |  |  |
| 35 | `TOTALHOURS` | DECIMAL(7,2) |  |  |  |  |
| 36 | `DATE1CODE` | CHAR(5) |  |  |  |  |
| 37 | `DATE1HOUR` | TIME |  |  |  |  |
| 38 | `DATE1BCODE` | CHAR(5) |  |  |  |  |
| 39 | `DATE1BHOUR` | TIME |  |  |  |  |
| 40 | `DATE2CODE` | CHAR(5) |  |  |  |  |
| 41 | `DATE2HOUR` | TIME |  |  |  |  |
| 42 | `DATE2BCODE` | CHAR(5) |  |  |  |  |
| 43 | `DATE2BHOUR` | TIME |  |  |  |  |
| 44 | `DATE3CODE` | CHAR(5) |  |  |  |  |
| 45 | `DATE3HOUR` | TIME |  |  |  |  |
| 46 | `DATE3BCODE` | CHAR(5) |  |  |  |  |
| 47 | `DATE3BHOUR` | TIME |  |  |  |  |
| 48 | `DATE4CODE` | CHAR(5) |  |  |  |  |
| 49 | `DATE4HOUR` | TIME |  |  |  |  |
| 50 | `DATE4BCODE` | CHAR(5) |  |  |  |  |
| 51 | `DATE4BHOUR` | TIME |  |  |  |  |
| 52 | `DATE5CODE` | CHAR(5) |  |  |  |  |
| 53 | `DATE5HOUR` | TIME |  |  |  |  |
| 54 | `DATE5BCODE` | CHAR(5) |  |  |  |  |
| 55 | `DATE5BHOUR` | TIME |  |  |  |  |
| 56 | `DATE6CODE` | CHAR(5) |  |  |  |  |
| 57 | `DATE6HOUR` | TIME |  |  |  |  |
| 58 | `DATE6BCODE` | CHAR(5) |  |  |  |  |
| 59 | `DATE6BHOUR` | TIME |  |  |  |  |
| 60 | `DATE7CODE` | CHAR(5) |  |  |  |  |
| 61 | `DATE7HOUR` | TIME |  |  |  |  |
| 62 | `DATE7BCODE` | CHAR(5) |  |  |  |  |
| 63 | `DATE7BHOUR` | TIME |  |  |  |  |
| 64 | `DATE8CODE` | CHAR(5) |  |  |  |  |
| 65 | `DATE8HOUR` | TIME |  |  |  |  |
| 66 | `DATE8BCODE` | CHAR(5) |  |  |  |  |
| 67 | `DATE8BHOUR` | TIME |  |  |  |  |
| 68 | `DATE9CODE` | CHAR(5) |  |  |  |  |
| 69 | `DATE9HOUR` | TIME |  |  |  |  |
| 70 | `DATE9BCODE` | CHAR(5) |  |  |  |  |
| 71 | `DATE9BHOUR` | TIME |  |  |  |  |
| 72 | `DATE10CODE` | CHAR(5) |  |  |  |  |
| 73 | `DATE10HOUR` | TIME |  |  |  |  |
| 74 | `DATE10BCODE` | CHAR(5) |  |  |  |  |
| 75 | `DATE10BHOUR` | TIME |  |  |  |  |
| 76 | `DATE11CODE` | CHAR(5) |  |  |  |  |
| 77 | `DATE11HOUR` | TIME |  |  |  |  |
| 78 | `DATE11BCODE` | CHAR(5) |  |  |  |  |
| 79 | `DATE11BHOUR` | TIME |  |  |  |  |
| 80 | `DATE12CODE` | CHAR(5) |  |  |  |  |
| 81 | `DATE12HOUR` | TIME |  |  |  |  |
| 82 | `DATE12BCODE` | CHAR(5) |  |  |  |  |
| 83 | `DATE12BHOUR` | TIME |  |  |  |  |
| 84 | `DATE13CODE` | CHAR(5) |  |  |  |  |
| 85 | `DATE13HOUR` | TIME |  |  |  |  |
| 86 | `DATE13BCODE` | CHAR(5) |  |  |  |  |
| 87 | `DATE13BHOUR` | TIME |  |  |  |  |
| 88 | `DATE14CODE` | CHAR(5) |  |  |  |  |
| 89 | `DATE14HOUR` | TIME |  |  |  |  |
| 90 | `DATE14BCODE` | CHAR(5) |  |  |  |  |
| 91 | `DATE14BHOUR` | TIME |  |  |  |  |
| 92 | `DATE15CODE` | CHAR(5) |  |  |  |  |
| 93 | `DATE15HOUR` | TIME |  |  |  |  |
| 94 | `DATE15BCODE` | CHAR(5) |  |  |  |  |
| 95 | `DATE15BHOUR` | TIME |  |  |  |  |
| 96 | `DATE16CODE` | CHAR(5) |  |  |  |  |
| 97 | `DATE16HOUR` | TIME |  |  |  |  |
| 98 | `DATE16BCODE` | CHAR(5) |  |  |  |  |
| 99 | `DATE16BHOUR` | TIME |  |  |  |  |
| 100 | `DATE17CODE` | CHAR(5) |  |  |  |  |
| 101 | `DATE17HOUR` | TIME |  |  |  |  |
| 102 | `DATE17BCODE` | CHAR(5) |  |  |  |  |
| 103 | `DATE17BHOUR` | TIME |  |  |  |  |
| 104 | `DATE18CODE` | CHAR(5) |  |  |  |  |
| 105 | `DATE18HOUR` | TIME |  |  |  |  |
| 106 | `DATE18BCODE` | CHAR(5) |  |  |  |  |
| 107 | `DATE18BHOUR` | TIME |  |  |  |  |
| 108 | `DATE19CODE` | CHAR(5) |  |  |  |  |
| 109 | `DATE19HOUR` | TIME |  |  |  |  |
| 110 | `DATE19BCODE` | CHAR(5) |  |  |  |  |
| 111 | `DATE19BHOUR` | TIME |  |  |  |  |
| 112 | `DATE20CODE` | CHAR(5) |  |  |  |  |
| 113 | `DATE20HOUR` | TIME |  |  |  |  |
| 114 | `DATE20BCODE` | CHAR(5) |  |  |  |  |
| 115 | `DATE20BHOUR` | TIME |  |  |  |  |
| 116 | `DATE21CODE` | CHAR(5) |  |  |  |  |
| 117 | `DATE21HOUR` | TIME |  |  |  |  |
| 118 | `DATE21BCODE` | CHAR(5) |  |  |  |  |
| 119 | `DATE21BHOUR` | TIME |  |  |  |  |
| 120 | `DATE22CODE` | CHAR(5) |  |  |  |  |
| 121 | `DATE22HOUR` | TIME |  |  |  |  |
| 122 | `DATE22BCODE` | CHAR(5) |  |  |  |  |
| 123 | `DATE22BHOUR` | TIME |  |  |  |  |
| 124 | `DATE23CODE` | CHAR(5) |  |  |  |  |
| 125 | `DATE23HOUR` | TIME |  |  |  |  |
| 126 | `DATE23BCODE` | CHAR(5) |  |  |  |  |
| 127 | `DATE23BHOUR` | TIME |  |  |  |  |
| 128 | `DATE24CODE` | CHAR(5) |  |  |  |  |
| 129 | `DATE24HOUR` | TIME |  |  |  |  |
| 130 | `DATE24BCODE` | CHAR(5) |  |  |  |  |
| 131 | `DATE24BHOUR` | TIME |  |  |  |  |
| 132 | `DATE25CODE` | CHAR(5) |  |  |  |  |
| 133 | `DATE25HOUR` | TIME |  |  |  |  |
| 134 | `DATE25BCODE` | CHAR(5) |  |  |  |  |
| 135 | `DATE25BHOUR` | TIME |  |  |  |  |
| 136 | `DATE26CODE` | CHAR(5) |  |  |  |  |
| 137 | `DATE26HOUR` | TIME |  |  |  |  |
| 138 | `DATE26BCODE` | CHAR(5) |  |  |  |  |
| 139 | `DATE26BHOUR` | TIME |  |  |  |  |
| 140 | `DATE27CODE` | CHAR(5) |  |  |  |  |
| 141 | `DATE27HOUR` | TIME |  |  |  |  |
| 142 | `DATE27BCODE` | CHAR(5) |  |  |  |  |
| 143 | `DATE27BHOUR` | TIME |  |  |  |  |
| 144 | `DATE28CODE` | CHAR(5) |  |  |  |  |
| 145 | `DATE28HOUR` | TIME |  |  |  |  |
| 146 | `DATE28BCODE` | CHAR(5) |  |  |  |  |
| 147 | `DATE28BHOUR` | TIME |  |  |  |  |
| 148 | `DATE29CODE` | CHAR(5) |  |  |  |  |
| 149 | `DATE29HOUR` | TIME |  |  |  |  |
| 150 | `DATE29BCODE` | CHAR(5) |  |  |  |  |
| 151 | `DATE29BHOUR` | TIME |  |  |  |  |
| 152 | `DATE30CODE` | CHAR(5) |  |  |  |  |
| 153 | `DATE30HOUR` | TIME |  |  |  |  |
| 154 | `DATE30BCODE` | CHAR(5) |  |  |  |  |
| 155 | `DATE30BHOUR` | TIME |  |  |  |  |
| 156 | `DATE31CODE` | CHAR(5) |  |  |  |  |
| 157 | `DATE31HOUR` | TIME |  |  |  |  |
| 158 | `DATE31BCODE` | CHAR(5) |  |  |  |  |
| 159 | `DATE31BHOUR` | TIME |  |  |  |  |
| 160 | `ATTENDANCETYPEDESC` | VARCHAR(200) |  |  |  |  |
| 161 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKEMPLOYEEREPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.COMPANYCODE,
       t.COMPANYDESCRIPTION,
       t.EMPLOYEECODE,
       t.LINE,
       t.CATEGORYCODE,
       t.CATEGORYDESCRIPTION,
       t.SUBCATEGORYCODE,
       t.SUBCATEGORYDESCRIPTION,
       t.WRKDAILYATTENDANCE,
       t.DIVISIONCODE
FROM   DB2ADMIN.WRKEMPLOYEEREPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
