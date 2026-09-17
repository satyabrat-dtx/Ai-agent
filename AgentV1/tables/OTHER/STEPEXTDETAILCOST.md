# DB2ADMIN.STEPEXTDETAILCOST

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 26
- **Primary key**: `COMPANYCODE`, `COUNTERCODE`, `CODE`, `STEPNUMBER`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 95130

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `STEPNUMBER` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 5 | `LINE` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 6 | `POCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 7 | `POCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 8 | `POCODE` | CHAR(15) |  |  |  |  |
| 9 | `POORDERDATE` | DATE |  |  |  |  |
| 10 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 11 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 12 | `SUPPLIERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 13 | `SUPPLIERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 14 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 15 | `COSTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 16 | `COSTTYPE` | CHAR(2) |  |  |  |  |
| 17 | `QUANTITYFATT` | DECIMAL(15,5) |  |  |  |  |
| 18 | `UNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 19 | `COSTELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 20 | `COSTELEMENTITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 21 | `COSTELEMENTSUBCODE01` | CHAR(20) |  |  |  |  |
| 22 | `SERVICECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 23 | `SERVICEITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 24 | `SERVICESUBCODE01` | CHAR(20) |  |  |  |  |
| 25 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `STEPEXTDETAILCOSTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.COUNTERCOMPANYCODE,
       t.COUNTERCODE,
       t.CODE,
       t.STEPNUMBER,
       t.LINE,
       t.POCOUNTERCOMPANYCODE,
       t.POCOUNTERCODE,
       t.POCODE,
       t.POORDERDATE,
       t.WORKCENTERCODE,
       t.OPERATIONCODE
FROM   DB2ADMIN.STEPEXTDETAILCOST t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
