# DB2ADMIN.INTERNALCUSTOMIZEDOPTIONS

- **Module**: `INTERNAL_ORDERS` (high confidence — table name starts with 'INTERNAL')
- **Roles**: `business_data`
- **Columns**: 34
- **Primary key**: `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 61458

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `TYPEPICKUPTIME` | CHAR(2) |  |  |  |  |
| 2 | `PICKUPDAYS` | INTEGER | NOT NULL |  |  |  |
| 3 | `TYPELEADTIME` | CHAR(2) |  |  |  |  |
| 4 | `TYPEPREPARATIONTIME` | CHAR(2) |  |  |  |  |
| 5 | `PREPARATIONDAYS` | INTEGER | NOT NULL |  |  |  |
| 6 | `APPROVERETURNDOCUMENT` | SMALLINT | NOT NULL |  |  |  |
| 7 | `ALLOWEDONLYTOTALSHIPMENT` | SMALLINT | NOT NULL |  |  |  |
| 8 | `INTDOCUMENTPRINTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 9 | `SPREADCHANGEORDERCODE` | CHAR(20) |  |  |  |  |
| 10 | `SPREADCHANGEDOCCODE` | CHAR(20) |  |  |  |  |
| 11 | `ORDERCOUNTERCODE` | CHAR(20) |  |  |  |  |
| 12 | `DOCUMENTCOUNTERCODE` | CHAR(20) |  |  |  |  |
| 13 | `RETURNCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 14 | `RETURNDEFINITIVECOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 15 | `PICKINGCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 16 | `CHECKORDERCODE` | CHAR(20) |  |  |  |  |
| 17 | `CHECKDOCUMENTCODE` | CHAR(20) |  |  |  |  |
| 18 | `ORDERCUSTOMIZEUICODE` | CHAR(20) |  |  |  |  |
| 19 | `INTDOCUMENTCUSTOMIZEUICODE` | CHAR(20) |  |  |  |  |
| 20 | `COPYDEPENDENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 21 | `CHECKORDERLINECODE` | CHAR(20) |  |  |  |  |
| 22 | `CHECKDOCUMENTLINECODE` | CHAR(20) |  |  |  |  |
| 23 | `LINECUSTOMIZEUICODE` | CHAR(20) |  |  |  |  |
| 24 | `DOCUMENTLINECUSTOMIZEUICODE` | CHAR(20) |  |  |  |  |
| 25 | `LINESPREADCHANGEORDERLINECODE` | CHAR(20) |  |  |  |  |
| 26 | `LINESPREADCHANGEDOCCODE` | CHAR(20) |  |  |  |  |
| 27 | `LINECLOSURERULECODE` | CHAR(20) |  |  |  |  |
| 28 | `DOCUMENTCLOSURERULECODE` | CHAR(20) |  |  |  |  |
| 29 | `CHECKORDERDELIVERYCODE` | CHAR(20) |  |  |  |  |
| 30 | `RETURNCOUNTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 31 | `RETURNDEFINITIVECNTCMYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 32 | `PICKINGCOUNTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 33 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `INTERNALCUSTOMIZEDOPTIONS.COMPANYCODE = COMPANY.CODE` |
| `COUNTER_PICKINGCOUNTER` | `PICKINGCOUNTERCOMPANYCODE`, `PICKINGCOUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `INTERNALCUSTOMIZEDOPTIONS.PICKINGCOUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND INTERNALCUSTOMIZEDOPTIONS.PICKINGCOUNTERCODE = COUNTER.CODE` |
| `COUNTER_RETURNCOUNTER` | `RETURNCOUNTERCOMPANYCODE`, `RETURNCOUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `INTERNALCUSTOMIZEDOPTIONS.RETURNCOUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND INTERNALCUSTOMIZEDOPTIONS.RETURNCOUNTERCODE = COUNTER.CODE` |
| `COUNTER_RETURNDEFINITIVECOUNTER` | `RETURNDEFINITIVECNTCMYCODE`, `RETURNDEFINITIVECOUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `INTERNALCUSTOMIZEDOPTIONS.RETURNDEFINITIVECNTCMYCODE = COUNTER.COMPANYCODE AND INTERNALCUSTOMIZEDOPTIONS.RETURNDEFINITIVECOUNTERCODE = COUNTER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `INTERNALCUSTOMIZEDOPTIONSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.TYPEPICKUPTIME,
       t.PICKUPDAYS,
       t.TYPELEADTIME,
       t.TYPEPREPARATIONTIME,
       t.PREPARATIONDAYS,
       t.APPROVERETURNDOCUMENT,
       t.ALLOWEDONLYTOTALSHIPMENT,
       t.INTDOCUMENTPRINTPOLICYCODE,
       t.SPREADCHANGEORDERCODE,
       t.SPREADCHANGEDOCCODE,
       t.ORDERCOUNTERCODE
FROM   DB2ADMIN.INTERNALCUSTOMIZEDOPTIONS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
