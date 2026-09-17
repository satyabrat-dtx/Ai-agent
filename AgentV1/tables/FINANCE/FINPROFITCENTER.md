# DB2ADMIN.FINPROFITCENTER

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 5 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 101723

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 10 | `GROUPFLAG` | SMALLINT | NOT NULL |  |  |  |
| 11 | `GROUPPCCODE` | CHAR(10) |  | FK | foreign_key |  |
| 12 | `VALIDITYFROM` | DATE | NOT NULL |  |  |  |
| 13 | `VALIDITYTO` | DATE | NOT NULL |  |  |  |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINPROFITCENTER.COMPANYCODE = COMPANY.CODE` |
| `FINPROFITCENTER_GROUPPC` | `COMPANYCODE`, `GROUPPCCODE` | [`FINPROFITCENTER`](../FINANCE/FINPROFITCENTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINPROFITCENTER.COMPANYCODE = FINPROFITCENTER.COMPANYCODE AND FINPROFITCENTER.GROUPPCCODE = FINPROFITCENTER.CODE` |

## Referenced by (child → this table) — 5

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `FINPROFITCENTER_PROFITCENTER` | [`FINVOULINESCRIT`](../FINANCE/FINVOULINESCRIT.md) | `FINVOULINFINVOUHDRCOMPANYCODE`, `PROFITCENTERCODE` | `FINVOULINESCRIT.FINVOULINFINVOUHDRCOMPANYCODE = FINPROFITCENTER.COMPANYCODE AND FINVOULINESCRIT.PROFITCENTERCODE = FINPROFITCENTER.CODE` |
| `FINPROFITCENTER_GROUPPC` | [`FINPROFITCENTER`](../FINANCE/FINPROFITCENTER.md) | `COMPANYCODE`, `GROUPPCCODE` | `FINPROFITCENTER.COMPANYCODE = FINPROFITCENTER.COMPANYCODE AND FINPROFITCENTER.GROUPPCCODE = FINPROFITCENTER.CODE` |
| `FINPROFITCENTER_PROFITCENTER` | [`GENERALLEDGERACCOUNT`](../FINANCE/GENERALLEDGERACCOUNT.md) | `COMPANYCODE`, `PROFITCENTERCODE` | `GENERALLEDGERACCOUNT.COMPANYCODE = FINPROFITCENTER.COMPANYCODE AND GENERALLEDGERACCOUNT.PROFITCENTERCODE = FINPROFITCENTER.CODE` |
| `FINPROFITCENTER_PROFITCENTER` | [`FINBUSINESSVSPROFIT`](../FINANCE/FINBUSINESSVSPROFIT.md) | `COMPANYCODE`, `PROFITCENTERCODE` | `FINBUSINESSVSPROFIT.COMPANYCODE = FINPROFITCENTER.COMPANYCODE AND FINBUSINESSVSPROFIT.PROFITCENTERCODE = FINPROFITCENTER.CODE` |
| `FINPROFITCENTER_PROFITCENTER` | [`FINBUVSCCVSPCDEFAULT`](../FINANCE/FINBUVSCCVSPCDEFAULT.md) | `COMPANYCODE`, `PROFITCENTERCODE` | `FINBUVSCCVSPCDEFAULT.COMPANYCODE = FINPROFITCENTER.COMPANYCODE AND FINBUVSCCVSPCDEFAULT.PROFITCENTERCODE = FINPROFITCENTER.CODE` |

## Indexes

- `FINPROFITCENTERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.GROUPFLAG,
       t.GROUPPCCODE
FROM   DB2ADMIN.FINPROFITCENTER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
