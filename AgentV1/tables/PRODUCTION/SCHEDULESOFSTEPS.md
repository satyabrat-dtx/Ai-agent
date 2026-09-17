# DB2ADMIN.SCHEDULESOFSTEPS

- **Module**: `PRODUCTION` (low confidence — FK neighbourhood: 1 of 1 related tables are PRODUCTION)
- **Roles**: `business_data`
- **Columns**: 35
- **Primary key**: `COMPANYCODE`, `COUNTERCODE`, `CODE`, `STEPNUMBER`, `HIGHLEVELSCHEDULE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 31784

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `STEPNUMBER` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 4 | `STEPISGROUPED` | CHAR(2) |  |  |  |  |
| 5 | `ENVIRONMENTCODE` | CHAR(3) |  |  |  |  |
| 6 | `FIRSTSCHEDULEGROUPNUMBERCODE` | CHAR(15) |  |  |  |  |
| 7 | `LOWESTSCHEDULELEVEL` | CHAR(2) |  |  |  |  |
| 8 | `HIGHESTSCHEDULELEVEL` | CHAR(2) |  |  |  |  |
| 9 | `SCHEDULEDONMANYWORKCENTERS` | CHAR(2) |  |  |  |  |
| 10 | `FIRSTSCHEDULEDWORKCENTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 11 | `TOTALQUANTITYSCHEDULEDINPRMUOM` | DECIMAL(15,5) |  |  |  |  |
| 12 | `PLANNEDSCHEDULEDQTYINPRMUOM` | DECIMAL(15,5) |  |  |  |  |
| 13 | `PRIMARYUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 14 | `TOTALSETUPTIMEBEFOREMATERIAL` | DECIMAL(11,2) |  |  |  |  |
| 15 | `TOTALSETUPTIMEAFTERMATERIAL` | DECIMAL(11,2) |  |  |  |  |
| 16 | `TOTALEXECUTIONTIME` | DECIMAL(15,5) |  |  |  |  |
| 17 | `LOWESTINITIALSCHEDULEDDATE` | DATE |  |  |  |  |
| 18 | `LOWESTINITIALSCHEDULEDTIME` | TIME |  |  |  |  |
| 19 | `HIGHESTFINALSCHEDULEDDATE` | DATE |  |  |  |  |
| 20 | `HIGHESTFINALSCHEDULEDTIME` | TIME |  |  |  |  |
| 21 | `UPDATED` | SMALLINT | NOT NULL |  |  |  |
| 22 | `ERRORTYPE` | CHAR(1) |  |  |  |  |
| 23 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 24 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 25 | `HIGHLEVELSCHEDULE` | SMALLINT | NOT NULL | PK | primary_key |  |
| 26 | `LOWESTINITSCHEDULEDACTUALDATE` | DATE |  |  |  |  |
| 27 | `LOWESTINITSCHEDULEDACTUALTIME` | TIME |  |  |  |  |
| 28 | `HIGHESTFINSCHEDULEDACTUALDATE` | DATE |  |  |  |  |
| 29 | `HIGHESTFINSCHEDULEDACTUALTIME` | TIME |  |  |  |  |
| 30 | `CALCULATEDATES` | SMALLINT | NOT NULL |  |  |  |
| 31 | `TORECALCULATE` | SMALLINT | NOT NULL |  |  |  |
| 32 | `THREADOPERATION` | CHAR(2) |  |  |  |  |
| 33 | `THREADLOCKNUMBER` | DECIMAL(7,0) |  |  |  |  |
| 34 | `THREADSTATUS` | CHAR(2) |  |  |  |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SCHEDULESOFSTEPS.COMPANYCODE = COMPANY.CODE` |
| `UNITOFMEASURE_PRIMARYUOM` | `PRIMARYUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `SCHEDULESOFSTEPS.PRIMARYUOMCODE = UNITOFMEASURE.CODE` |
| `WORKCENTER_FIRSTSCHEDULEDWORKCENTER` | `COMPANYCODE`, `FIRSTSCHEDULEDWORKCENTERCODE` | [`WORKCENTER`](../PRODUCTION/WORKCENTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SCHEDULESOFSTEPS.COMPANYCODE = WORKCENTER.COMPANYCODE AND SCHEDULESOFSTEPS.FIRSTSCHEDULEDWORKCENTERCODE = WORKCENTER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SCHEDULESOFSTEPSUID` (ABSUNIQUEID)
- `SCHEDULESOFSTEPS01` (TORECALCULATE, ENVIRONMENTCODE, COMPANYCODE)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.COUNTERCODE,
       t.CODE,
       t.STEPNUMBER,
       t.STEPISGROUPED,
       t.ENVIRONMENTCODE,
       t.FIRSTSCHEDULEGROUPNUMBERCODE,
       t.LOWESTSCHEDULELEVEL,
       t.HIGHESTSCHEDULELEVEL,
       t.SCHEDULEDONMANYWORKCENTERS,
       t.FIRSTSCHEDULEDWORKCENTERCODE,
       t.TOTALQUANTITYSCHEDULEDINPRMUOM
FROM   DB2ADMIN.SCHEDULESOFSTEPS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
