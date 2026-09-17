# DB2ADMIN.PMAUTOWORKORDERHISTORY

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `COMPANYCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 88699

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `PLANTCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 3 | `PLANTCODE` | CHAR(8) |  | FK | foreign_key |  |
| 4 | `FROMDATE` | DATE | NOT NULL |  |  | Inclusive start of a validity period. |
| 5 | `TODATE` | DATE | NOT NULL |  |  | End of a validity period. |
| 6 | `PRVCOUNTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `PRVCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 8 | `WORKORDERCOUNTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 9 | `WORKORDERCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 10 | `EMAIL` | CHAR(50) |  |  |  |  |
| 11 | `HALLNOUSERGENGRPTYPECMYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `HALLNOUSERGENERICGROUPTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 13 | `HALLNOCODE` | CHAR(10) |  | FK | foreign_key |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PMAUTOWORKORDERHISTORY.COMPANYCODE = COMPANY.CODE` |
| `COUNTER_PRVCOUNTER` | `PRVCOUNTERCOMPANYCODE`, `PRVCOUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMAUTOWORKORDERHISTORY.PRVCOUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND PMAUTOWORKORDERHISTORY.PRVCOUNTERCODE = COUNTER.CODE` |
| `COUNTER_WORKORDERCOUNTER` | `WORKORDERCOUNTERCOMPANYCODE`, `WORKORDERCOUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMAUTOWORKORDERHISTORY.WORKORDERCOUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND PMAUTOWORKORDERHISTORY.WORKORDERCOUNTERCODE = COUNTER.CODE` |
| `PLANT_PLANT` | `PLANTCOMPANYCODE`, `PLANTCODE` | [`PLANT`](../CORE_MASTER/PLANT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMAUTOWORKORDERHISTORY.PLANTCOMPANYCODE = PLANT.COMPANYCODE AND PMAUTOWORKORDERHISTORY.PLANTCODE = PLANT.CODE` |
| `USERGENERICGROUP_HALLNO` | `HALLNOUSERGENGRPTYPECMYCODE`, `HALLNOUSERGENERICGROUPTYPECODE`, `HALLNOCODE` | [`USERGENERICGROUP`](../CORE_MASTER/USERGENERICGROUP.md) | `USERGENGROUPTYPECOMPANYCODE`, `USERGENERICGROUPTYPECODE`, `CODE` | RESTRICT | `PMAUTOWORKORDERHISTORY.HALLNOUSERGENGRPTYPECMYCODE = USERGENERICGROUP.USERGENGROUPTYPECOMPANYCODE AND PMAUTOWORKORDERHISTORY.HALLNOUSERGENERICGROUPTYPECODE = USERGENERICGROUP.USERGENERICGROUPTYPECODE AND PMAUTOWORKORDERHISTORY.HALLNOCODE = USERGENERICGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PMAUTOWORKORDERHISTORYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.LINENO,
       t.PLANTCOMPANYCODE,
       t.PLANTCODE,
       t.FROMDATE,
       t.TODATE,
       t.PRVCOUNTERCOMPANYCODE,
       t.PRVCOUNTERCODE,
       t.WORKORDERCOUNTERCOMPANYCODE,
       t.WORKORDERCOUNTERCODE,
       t.EMAIL,
       t.HALLNOUSERGENGRPTYPECMYCODE
FROM   DB2ADMIN.PMAUTOWORKORDERHISTORY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
