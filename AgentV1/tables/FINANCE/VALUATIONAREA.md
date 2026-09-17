# DB2ADMIN.VALUATIONAREA

- **Module**: `FINANCE` (low confidence — FK neighbourhood: 2 of 2 related tables are FINANCE)
- **Roles**: `business_data`
- **Columns**: 27
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 2 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 103314

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(100) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `COMMERCIALLAW` | SMALLINT | NOT NULL |  |  |  |
| 6 | `TAXLAW` | SMALLINT | NOT NULL |  |  |  |
| 7 | `IMPUTED` | SMALLINT | NOT NULL |  |  |  |
| 8 | `GROUPLAW` | SMALLINT | NOT NULL |  |  |  |
| 9 | `FOREIGNCURRCODECODE` | CHAR(4) |  | FK | foreign_key |  |
| 10 | `MAXRATEDECLDEPR` | DECIMAL(5,3) | NOT NULL |  |  |  |
| 11 | `MAXFACSTRLINE` | DECIMAL(3,2) | NOT NULL |  |  |  |
| 12 | `WRITEOFFNBV` | SMALLINT | NOT NULL |  |  |  |
| 13 | `CONTINUEAFTEREND` | SMALLINT | NOT NULL |  |  |  |
| 14 | `ROUNDDEPRECIATION` | CHAR(3) |  |  |  |  |
| 15 | `ROUNDVALUE` | DECIMAL(5,2) |  |  |  |  |
| 16 | `DEPRECCOMMENCEMNT` | CHAR(3) | NOT NULL |  |  |  |
| 17 | `INPUTDIVIDER` | DECIMAL(5,2) |  |  |  |  |
| 18 | `HIDDENRESERVES` | SMALLINT | NOT NULL |  |  |  |
| 19 | `YEARSINOPERASSET` | DECIMAL(2,0) |  |  |  |  |
| 20 | `SPECIALITEM` | SMALLINT | NOT NULL |  |  |  |
| 21 | `REVALUATION` | SMALLINT | NOT NULL |  |  |  |
| 22 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 23 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 24 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 25 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 26 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `VALUATIONAREA.COMPANYCODE = COMPANY.CODE` |
| `CURRENCY_FOREIGNCURRCODE` | `FOREIGNCURRCODECODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `VALUATIONAREA.FOREIGNCURRCODECODE = CURRENCY.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `VALUATIONAREA_VALUATIONAREA` | [`ASSETGROUPVALAREADEFAULTS`](../FINANCE/ASSETGROUPVALAREADEFAULTS.md) | `ASSETGROUPCOMPANYCODE`, `VALUATIONAREACODE` | `ASSETGROUPVALAREADEFAULTS.ASSETGROUPCOMPANYCODE = VALUATIONAREA.COMPANYCODE AND ASSETGROUPVALAREADEFAULTS.VALUATIONAREACODE = VALUATIONAREA.CODE` |
| `VALUATIONAREA_VALUATIONAREA` | [`ASSETVALUATIONAREA`](../FINANCE/ASSETVALUATIONAREA.md) | `ASSETMASTERCOMPANYCODE`, `VALUATIONAREACODE` | `ASSETVALUATIONAREA.ASSETMASTERCOMPANYCODE = VALUATIONAREA.COMPANYCODE AND ASSETVALUATIONAREA.VALUATIONAREACODE = VALUATIONAREA.CODE` |

## Indexes

- `VALUATIONAREAUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.COMMERCIALLAW,
       t.TAXLAW,
       t.IMPUTED,
       t.GROUPLAW,
       t.FOREIGNCURRCODECODE,
       t.MAXRATEDECLDEPR,
       t.MAXFACSTRLINE
FROM   DB2ADMIN.VALUATIONAREA t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
