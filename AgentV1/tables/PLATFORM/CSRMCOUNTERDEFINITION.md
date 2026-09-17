# DB2ADMIN.CSRMCOUNTERDEFINITION

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 1 of 1 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `NUMBERID`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 118488

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `NUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 2 | `ORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 3 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 4 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `STATISTICALGROUPCODE` | CHAR(6) |  | FK | foreign_key |  |
| 6 | `CSRMTEMPLATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `COUNTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `COUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `CSRMCOUNTERDEFINITION.COMPANYCODE = COMPANY.CODE` |
| `COUNTER_COUNTER` | `COUNTERCOMPANYCODE`, `COUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CSRMCOUNTERDEFINITION.COUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND CSRMCOUNTERDEFINITION.COUNTERCODE = COUNTER.CODE` |
| `CSRMTEMPLATE_CSRMTEMPLATE` | `COMPANYCODE`, `CSRMTEMPLATECODE` | [`CSRMTEMPLATE`](../PLATFORM/CSRMTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CSRMCOUNTERDEFINITION.COMPANYCODE = CSRMTEMPLATE.COMPANYCODE AND CSRMCOUNTERDEFINITION.CSRMTEMPLATECODE = CSRMTEMPLATE.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CSRMCOUNTERDEFINITION.COMPANYCODE = DIVISION.COMPANYCODE AND CSRMCOUNTERDEFINITION.DIVISIONCODE = DIVISION.CODE` |
| `STATISTICALGROUP_STATISTICALGROUP` | `STATISTICALGROUPCOMPANYCODE`, `STATISTICALGROUPCODE` | [`STATISTICALGROUP`](../CORE_MASTER/STATISTICALGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CSRMCOUNTERDEFINITION.STATISTICALGROUPCOMPANYCODE = STATISTICALGROUP.COMPANYCODE AND CSRMCOUNTERDEFINITION.STATISTICALGROUPCODE = STATISTICALGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CSRMCOUNTERDEFINITIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.NUMBERID,
       t.ORDERTYPE,
       t.DIVISIONCODE,
       t.STATISTICALGROUPCOMPANYCODE,
       t.STATISTICALGROUPCODE,
       t.CSRMTEMPLATECODE,
       t.COUNTERCOMPANYCODE,
       t.COUNTERCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.CSRMCOUNTERDEFINITION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
