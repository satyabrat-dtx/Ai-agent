# DB2ADMIN.ARTICLESTATUS

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `ITEMTYPECODE`, `CODE`
- **FK degree**: referenced by 6 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 189965

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 2 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `CODE` | CHAR(8) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `ALWAYSAPPLY` | SMALLINT | NOT NULL |  |  |  |
| 8 | `REASONCODEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ARTICLESTATUS.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ARTICLESTATUS.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND ARTICLESTATUS.ITEMTYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 6

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ARTICLESTATUS_ARTICLESTATUS` | [`DESIGN`](../PRODUCTION/DESIGN.md) | `COMPANYCODE`, `ITEMTYPECODE`, `ARTICLESTATUSCODE` | `DESIGN.COMPANYCODE = ARTICLESTATUS.COMPANYCODE AND DESIGN.ITEMTYPECODE = ARTICLESTATUS.ITEMTYPECODE AND DESIGN.ARTICLESTATUSCODE = ARTICLESTATUS.CODE` |
| `ARTICLESTATUS_ARTICLESTATUS` | [`PATTERN`](../PRODUCTION/PATTERN.md) | `COMPANYCODE`, `ITEMTYPECODE`, `ARTICLESTATUSCODE` | `PATTERN.COMPANYCODE = ARTICLESTATUS.COMPANYCODE AND PATTERN.ITEMTYPECODE = ARTICLESTATUS.ITEMTYPECODE AND PATTERN.ARTICLESTATUSCODE = ARTICLESTATUS.CODE` |
| `ARTICLESTATUS_ARTICLESTATUS` | [`PRODUCT`](../ITEM_MASTER/PRODUCT.md) | `COMPANYCODE`, `ITEMTYPECODE`, `ARTICLESTATUSCODE` | `PRODUCT.COMPANYCODE = ARTICLESTATUS.COMPANYCODE AND PRODUCT.ITEMTYPECODE = ARTICLESTATUS.ITEMTYPECODE AND PRODUCT.ARTICLESTATUSCODE = ARTICLESTATUS.CODE` |
| `ARTICLESTATUS_ARTICLESTATUS` | [`FULLITEMKEYDECODER`](../COSTING/FULLITEMKEYDECODER.md) | `COMPANYCODE`, `ITEMTYPECODE`, `ARTICLESTATUSCODE` | `FULLITEMKEYDECODER.COMPANYCODE = ARTICLESTATUS.COMPANYCODE AND FULLITEMKEYDECODER.ITEMTYPECODE = ARTICLESTATUS.ITEMTYPECODE AND FULLITEMKEYDECODER.ARTICLESTATUSCODE = ARTICLESTATUS.CODE` |
| `ARTICLESTATUS_ARTICLESTATUS` | [`RECIPE`](../COSTING/RECIPE.md) | `COMPANYCODE`, `ITEMTYPECODE`, `ARTICLESTATUSCODE` | `RECIPE.COMPANYCODE = ARTICLESTATUS.COMPANYCODE AND RECIPE.ITEMTYPECODE = ARTICLESTATUS.ITEMTYPECODE AND RECIPE.ARTICLESTATUSCODE = ARTICLESTATUS.CODE` |
| `ARTICLESTATUS_STATUSRULELIST` | [`STATUSRULE`](../OTHER/STATUSRULE.md) | `ARTICLESTATUSCOMPANYCODE`, `ARTICLESTATUSITEMTYPECODE`, `ARTICLESTATUSCODE` | `STATUSRULE.ARTICLESTATUSCOMPANYCODE = ARTICLESTATUS.COMPANYCODE AND STATUSRULE.ARTICLESTATUSITEMTYPECODE = ARTICLESTATUS.ITEMTYPECODE AND STATUSRULE.ARTICLESTATUSCODE = ARTICLESTATUS.CODE` |

## Indexes

- `ARTICLESTATUSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ALWAYSAPPLY,
       t.REASONCODEREQUIRED,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.ARTICLESTATUS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
