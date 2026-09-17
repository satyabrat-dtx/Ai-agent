# DB2ADMIN.EXTOPLINEIE

- **Module**: `SUBCONTRACTING` (medium confidence — table name starts with 'EXTOP')
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `COMPANYCODE`, `COUNTERCODE`, `CODE`, `ORDERLINE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 130474

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 2 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `ORDERLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 5 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 6 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 7 | `TARIFFCODE` | CHAR(20) |  | FK | foreign_key |  |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 9 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 10 | `GROSSVALUEWOHEADER` | DECIMAL(18,5) |  |  |  |  |
| 11 | `GROSSVALUEEXT` | DECIMAL(18,5) |  |  |  |  |
| 12 | `SELECTIONDATE` | DATE |  |  |  |  |
| 13 | `ADVANCEOPTION` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `EXTOPLINEIE.COMPANYCODE = COMPANY.CODE` |
| `COUNTER_COUNTER` | `COUNTERCOMPANYCODE`, `COUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EXTOPLINEIE.COUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND EXTOPLINEIE.COUNTERCODE = COUNTER.CODE` |
| `TARIFF_TARIFF` | `TARIFFCODE` | [`TARIFF`](../CORE_MASTER/TARIFF.md) | `CODE` | RESTRICT | `EXTOPLINEIE.TARIFFCODE = TARIFF.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EXTOPLINEIEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.COUNTERCOMPANYCODE,
       t.COUNTERCODE,
       t.CODE,
       t.ORDERLINE,
       t.TAXTEMPLATETEMPLATETYPE,
       t.TAXTEMPLATECODE,
       t.TARIFFCODE,
       t.ABSUNIQUEID,
       t.BASICVALUE,
       t.GROSSVALUEWOHEADER,
       t.GROSSVALUEEXT
FROM   DB2ADMIN.EXTOPLINEIE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
