# DB2ADMIN.PRODUCTGROUPING

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'PRODUCT')
- **Roles**: `business_data`
- **Columns**: 36
- **Primary key**: `COMPANYCODE`, `ANALYSISCODE`, `ARTICLETYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 125378

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ANALYSISCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ARTICLETYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 3 | `ARTICLETYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `ITEMTYPE` | SMALLINT | NOT NULL |  |  |  |
| 5 | `ITEMTYPEWTSC` | SMALLINT | NOT NULL |  |  |  |
| 6 | `SUBCODE` | CHAR(3) |  |  |  |  |
| 7 | `ITEMTYPEWTUGRP` | SMALLINT | NOT NULL |  |  |  |
| 8 | `USERGROUP` | CHAR(3) |  |  |  |  |
| 9 | `ITEMTYPE2` | SMALLINT | NOT NULL |  |  |  |
| 10 | `ITEMTYPEWTSC1` | SMALLINT | NOT NULL |  |  |  |
| 11 | `SUBCODE1` | CHAR(3) |  |  |  |  |
| 12 | `ITEMTYPEWTUGRP1` | SMALLINT | NOT NULL |  |  |  |
| 13 | `USERGROUP1` | CHAR(3) |  |  |  |  |
| 14 | `ITEMTYPE3` | SMALLINT | NOT NULL |  |  |  |
| 15 | `ITEMTYPEWTSC2` | SMALLINT | NOT NULL |  |  |  |
| 16 | `SUBCODE2` | CHAR(3) |  |  |  |  |
| 17 | `ITEMTYPEWTUGRP2` | SMALLINT | NOT NULL |  |  |  |
| 18 | `USERGROUP2` | CHAR(3) |  |  |  |  |
| 19 | `ITEMTYPE4` | SMALLINT | NOT NULL |  |  |  |
| 20 | `ITEMTYPEWTSC3` | SMALLINT | NOT NULL |  |  |  |
| 21 | `SUBCODE3` | CHAR(3) |  |  |  |  |
| 22 | `ITEMTYPEWTUGRP3` | SMALLINT | NOT NULL |  |  |  |
| 23 | `USERGROUP3` | CHAR(3) |  |  |  |  |
| 24 | `ITEMTYPE5` | SMALLINT | NOT NULL |  |  |  |
| 25 | `ITEMTYPEWTSC4` | SMALLINT | NOT NULL |  |  |  |
| 26 | `SUBCODE4` | CHAR(3) |  |  |  |  |
| 27 | `ITEMTYPEWTUGRP4` | SMALLINT | NOT NULL |  |  |  |
| 28 | `USERGROUP4` | CHAR(3) |  |  |  |  |
| 29 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 30 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 31 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 32 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 33 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 34 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 35 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ANALYSISTYPE_ANALYSIS` | `COMPANYCODE`, `ANALYSISCODE` | [`ANALYSISTYPE`](../ITEM_MASTER/ANALYSISTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRODUCTGROUPING.COMPANYCODE = ANALYSISTYPE.COMPANYCODE AND PRODUCTGROUPING.ANALYSISCODE = ANALYSISTYPE.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PRODUCTGROUPING.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ARTICLETYPE` | `ARTICLETYPECOMPANYCODE`, `ARTICLETYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRODUCTGROUPING.ARTICLETYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND PRODUCTGROUPING.ARTICLETYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRODUCTGROUPINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ANALYSISCODE,
       t.ARTICLETYPECOMPANYCODE,
       t.ARTICLETYPECODE,
       t.ITEMTYPE,
       t.ITEMTYPEWTSC,
       t.SUBCODE,
       t.ITEMTYPEWTUGRP,
       t.USERGROUP,
       t.ITEMTYPE2,
       t.ITEMTYPEWTSC1,
       t.SUBCODE1
FROM   DB2ADMIN.PRODUCTGROUPING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
