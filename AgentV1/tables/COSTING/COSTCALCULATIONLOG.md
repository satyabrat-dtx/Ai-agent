# DB2ADMIN.COSTCALCULATIONLOG

- **Module**: `COSTING` (high confidence — table name starts with 'COST')
- **Roles**: `business_data`
- **Columns**: 54
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `CREATIONUSER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 9389

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `CREATIONUSER` | CHAR(25) | NOT NULL | PK | primary_key audit | User who created the row (audit). |
| 3 | `STATUS` | CHAR(2) | NOT NULL |  |  |  |
| 4 | `PROGRESSSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 5 | `EVALUATIONSTEP` | CHAR(2) | NOT NULL |  |  |  |
| 6 | `USERUSERID` | CHAR(25) |  |  |  |  |
| 7 | `LOGCREATIONTIMESTAMP` | BIGINT |  |  |  |  |
| 8 | `LOGCREATIONUSER` | CHAR(25) |  |  |  |  |
| 9 | `RESTOREPREVIOUSCOST` | SMALLINT | NOT NULL |  |  |  |
| 10 | `RUNBATCH` | SMALLINT | NOT NULL |  |  |  |
| 11 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 12 | `COSTGROUP1CODE` | CHAR(3) | NOT NULL |  |  |  |
| 13 | `LOWLEVELUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 14 | `PURCHASEEVALUATION` | SMALLINT | NOT NULL |  |  |  |
| 15 | `CALCULATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 16 | `COMPONENTCOSTEVALUATION` | CHAR(2) | NOT NULL |  |  |  |
| 17 | `MATERIALCOSTEVALUATION` | SMALLINT | NOT NULL |  |  |  |
| 18 | `OTHERCOSTELEMENTSEVALUATION` | SMALLINT | NOT NULL |  |  |  |
| 19 | `OPERATIONEVALUATION` | SMALLINT | NOT NULL |  |  |  |
| 20 | `TOOLCOSTEVALUATION` | SMALLINT | NOT NULL |  |  |  |
| 21 | `PERSONALIZEDFINISHEVALUATION` | SMALLINT | NOT NULL |  |  |  |
| 22 | `UPDATECOST` | SMALLINT | NOT NULL |  |  |  |
| 23 | `PRINTCHANGEDCOST` | SMALLINT | NOT NULL |  |  |  |
| 24 | `COSTCHANGEPERCENTAGELIMIT` | DECIMAL(5,2) |  |  |  |  |
| 25 | `PRINTDETAILEDCOSTLIST` | SMALLINT | NOT NULL |  |  |  |
| 26 | `COSTGROUP2CODE` | CHAR(3) |  |  |  |  |
| 27 | `COSTGROUP3CODE` | CHAR(3) |  |  |  |  |
| 28 | `COSTGROUP4CODE` | CHAR(3) |  |  |  |  |
| 29 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 30 | `SUBCODESWITHOUTCHECK` | SMALLINT | NOT NULL |  |  |  |
| 31 | `INITIALSUBCODE01` | CHAR(20) |  |  |  |  |
| 32 | `INITIALSUBCODE02` | CHAR(10) |  |  |  |  |
| 33 | `INITIALSUBCODE03` | CHAR(10) |  |  |  |  |
| 34 | `INITIALSUBCODE04` | CHAR(10) |  |  |  |  |
| 35 | `INITIALSUBCODE05` | CHAR(10) |  |  |  |  |
| 36 | `INITIALSUBCODE06` | CHAR(10) |  |  |  |  |
| 37 | `INITIALSUBCODE07` | CHAR(10) |  |  |  |  |
| 38 | `INITIALSUBCODE08` | CHAR(10) |  |  |  |  |
| 39 | `INITIALSUBCODE09` | CHAR(10) |  |  |  |  |
| 40 | `INITIALSUBCODE10` | CHAR(10) |  |  |  |  |
| 41 | `DISPLAYFINALITEMCODE` | SMALLINT | NOT NULL |  |  |  |
| 42 | `FINALSUBCODE01` | CHAR(20) |  |  |  |  |
| 43 | `FINALSUBCODE02` | CHAR(10) |  |  |  |  |
| 44 | `FINALSUBCODE03` | CHAR(10) |  |  |  |  |
| 45 | `FINALSUBCODE04` | CHAR(10) |  |  |  |  |
| 46 | `FINALSUBCODE05` | CHAR(10) |  |  |  |  |
| 47 | `FINALSUBCODE06` | CHAR(10) |  |  |  |  |
| 48 | `FINALSUBCODE07` | CHAR(10) |  |  |  |  |
| 49 | `FINALSUBCODE08` | CHAR(10) |  |  |  |  |
| 50 | `FINALSUBCODE09` | CHAR(10) |  |  |  |  |
| 51 | `FINALSUBCODE10` | CHAR(10) |  |  |  |  |
| 52 | `VALIDUNTILDATE` | DATE |  |  |  |  |
| 53 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.STATUS,
       t.PROGRESSSTATUS,
       t.EVALUATIONSTEP,
       t.USERUSERID,
       t.LOGCREATIONTIMESTAMP,
       t.LOGCREATIONUSER,
       t.RESTOREPREVIOUSCOST,
       t.RUNBATCH,
       t.PLANTCODE
FROM   DB2ADMIN.COSTCALCULATIONLOG t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
