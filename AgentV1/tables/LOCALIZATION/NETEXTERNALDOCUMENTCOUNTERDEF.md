# DB2ADMIN.NETEXTERNALDOCUMENTCOUNTERDEF

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'NET')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `COMPANYCODE`, `PLANTCODE`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 199518

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `PLANTCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 3 | `PLANTCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `COUNTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `COUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 6 | `EXTOPERATIONDOCCNTDEFCMYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `EXTOPERATIONDOCCOUNTERDEFCODE` | CHAR(8) |  | FK | foreign_key |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `NETEXTERNALDOCUMENTCOUNTERDEF.COMPANYCODE = COMPANY.CODE` |
| `COUNTER_COUNTER` | `COUNTERCOMPANYCODE`, `COUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `NETEXTERNALDOCUMENTCOUNTERDEF.COUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND NETEXTERNALDOCUMENTCOUNTERDEF.COUNTERCODE = COUNTER.CODE` |
| `COUNTER_EXTOPERATIONDOCCOUNTERDEF` | `EXTOPERATIONDOCCNTDEFCMYCODE`, `EXTOPERATIONDOCCOUNTERDEFCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `NETEXTERNALDOCUMENTCOUNTERDEF.EXTOPERATIONDOCCNTDEFCMYCODE = COUNTER.COMPANYCODE AND NETEXTERNALDOCUMENTCOUNTERDEF.EXTOPERATIONDOCCOUNTERDEFCODE = COUNTER.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `NETEXTERNALDOCUMENTCOUNTERDEF.COMPANYCODE = DIVISION.COMPANYCODE AND NETEXTERNALDOCUMENTCOUNTERDEF.DIVISIONCODE = DIVISION.CODE` |
| `PLANT_PLANT` | `PLANTCOMPANYCODE`, `PLANTCODE` | [`PLANT`](../CORE_MASTER/PLANT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `NETEXTERNALDOCUMENTCOUNTERDEF.PLANTCOMPANYCODE = PLANT.COMPANYCODE AND NETEXTERNALDOCUMENTCOUNTERDEF.PLANTCODE = PLANT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `NETEXTERNALDOCCOUNTERDEFUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.PLANTCOMPANYCODE,
       t.PLANTCODE,
       t.COUNTERCOMPANYCODE,
       t.COUNTERCODE,
       t.EXTOPERATIONDOCCNTDEFCMYCODE,
       t.EXTOPERATIONDOCCOUNTERDEFCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.NETEXTERNALDOCUMENTCOUNTERDEF t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
