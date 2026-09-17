# DB2ADMIN.PRODUCTIONCOUNTERDEFINITION

- **Module**: `PRODUCTION` (high confidence — table name starts with 'PRODUCTION')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `NUMBERID`
- **FK degree**: referenced by 0 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 26095

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `NUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 2 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 3 | `STATISTICALGROUPCODE` | CHAR(6) |  | FK | foreign_key |  |
| 4 | `PRODUCTIONDEMANDTEMPLATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `COUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 13 | `COUNTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PRODUCTIONCOUNTERDEFINITION.COMPANYCODE = COMPANY.CODE` |
| `COUNTER_COUNTER` | `COUNTERCOMPANYCODE`, `COUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRODUCTIONCOUNTERDEFINITION.COUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND PRODUCTIONCOUNTERDEFINITION.COUNTERCODE = COUNTER.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRODUCTIONCOUNTERDEFINITION.COMPANYCODE = DIVISION.COMPANYCODE AND PRODUCTIONCOUNTERDEFINITION.DIVISIONCODE = DIVISION.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRODUCTIONCOUNTERDEFINITION.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND PRODUCTIONCOUNTERDEFINITION.ITEMTYPECODE = ITEMTYPE.CODE` |
| `PRODUCTIONDEMANDTEMPLATE_PRODUCTIONDEMANDTEMPLATE` | `COMPANYCODE`, `PRODUCTIONDEMANDTEMPLATECODE` | [`PRODUCTIONDEMANDTEMPLATE`](../PRODUCTION/PRODUCTIONDEMANDTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRODUCTIONCOUNTERDEFINITION.COMPANYCODE = PRODUCTIONDEMANDTEMPLATE.COMPANYCODE AND PRODUCTIONCOUNTERDEFINITION.PRODUCTIONDEMANDTEMPLATECODE = PRODUCTIONDEMANDTEMPLATE.CODE` |
| `STATISTICALGROUP_STATISTICALGROUP` | `STATISTICALGROUPCOMPANYCODE`, `STATISTICALGROUPCODE` | [`STATISTICALGROUP`](../CORE_MASTER/STATISTICALGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRODUCTIONCOUNTERDEFINITION.STATISTICALGROUPCOMPANYCODE = STATISTICALGROUP.COMPANYCODE AND PRODUCTIONCOUNTERDEFINITION.STATISTICALGROUPCODE = STATISTICALGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PROCOUNTERDEFINITIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.NUMBERID,
       t.DIVISIONCODE,
       t.STATISTICALGROUPCODE,
       t.PRODUCTIONDEMANDTEMPLATECODE,
       t.ITEMTYPECODE,
       t.COUNTERCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.STATISTICALGROUPCOMPANYCODE
FROM   DB2ADMIN.PRODUCTIONCOUNTERDEFINITION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
