# DB2ADMIN.PRHEADERCOUNTERMAP

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `PLANTCODE`, `REQUISITIONTEMPLATECODE`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 129664

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `PLANTCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 3 | `PLANTCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `REQUISITIONTEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `PRHEADERCOUNTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `PRHEADERCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PRHEADERCOUNTERMAP.COMPANYCODE = COMPANY.CODE` |
| `COUNTER_PRHEADERCOUNTER` | `PRHEADERCOUNTERCOMPANYCODE`, `PRHEADERCOUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRHEADERCOUNTERMAP.PRHEADERCOUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND PRHEADERCOUNTERMAP.PRHEADERCOUNTERCODE = COUNTER.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRHEADERCOUNTERMAP.COMPANYCODE = DIVISION.COMPANYCODE AND PRHEADERCOUNTERMAP.DIVISIONCODE = DIVISION.CODE` |
| `PLANT_PLANT` | `PLANTCOMPANYCODE`, `PLANTCODE` | [`PLANT`](../CORE_MASTER/PLANT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRHEADERCOUNTERMAP.PLANTCOMPANYCODE = PLANT.COMPANYCODE AND PRHEADERCOUNTERMAP.PLANTCODE = PLANT.CODE` |
| `REQUISITIONTEMPLATE_REQUISITIONTEMPLATE` | `COMPANYCODE`, `REQUISITIONTEMPLATECODE` | [`REQUISITIONTEMPLATE`](../CORE_MASTER/REQUISITIONTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRHEADERCOUNTERMAP.COMPANYCODE = REQUISITIONTEMPLATE.COMPANYCODE AND PRHEADERCOUNTERMAP.REQUISITIONTEMPLATECODE = REQUISITIONTEMPLATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRHEADERCOUNTERMAPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.PLANTCOMPANYCODE,
       t.PLANTCODE,
       t.REQUISITIONTEMPLATECODE,
       t.PRHEADERCOUNTERCOMPANYCODE,
       t.PRHEADERCOUNTERCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.PRHEADERCOUNTERMAP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
