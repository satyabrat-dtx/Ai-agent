# DB2ADMIN.WASTEGENERATIONTEMPLATES

- **Module**: `QUALITY` (low confidence — FK neighbourhood: 1 of 1 related tables are QUALITY)
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `COMPANYCODE`, `ANALYSISTYPECODE`, `GROUPID`, `ITEMTYPECODE`, `QUALITYCODE`, `FLAG`, `PRODPRGTEMPLATECODE`, `STKTRANSTEMPLATECODE`, `WAREHOUSECODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 126282

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ANALYSISTYPECODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `GROUPID` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 4 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `QUALITYITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 6 | `QUALITYCODE` | DECIMAL(2,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 7 | `FLAG` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 8 | `PRODPRGTEMPLATECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 9 | `STKTRANSTEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 10 | `STKTRANSTEMPLATECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 11 | `WAREHOUSECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 12 | `WAREHOUSECODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 20 | `PRODPRGTEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ANALYSISTYPE_ANALYSISTYPE` | `COMPANYCODE`, `ANALYSISTYPECODE` | [`ANALYSISTYPE`](../ITEM_MASTER/ANALYSISTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `WASTEGENERATIONTEMPLATES.COMPANYCODE = ANALYSISTYPE.COMPANYCODE AND WASTEGENERATIONTEMPLATES.ANALYSISTYPECODE = ANALYSISTYPE.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `WASTEGENERATIONTEMPLATES.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `WASTEGENERATIONTEMPLATES.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND WASTEGENERATIONTEMPLATES.ITEMTYPECODE = ITEMTYPE.CODE` |
| `QUALITYLEVEL_QUALITY` | `QUALITYITEMTYPECOMPANYCODE`, `ITEMTYPECODE`, `QUALITYCODE` | [`QUALITYLEVEL`](../QUALITY/QUALITYLEVEL.md) | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE`, `CODE` | RESTRICT | `WASTEGENERATIONTEMPLATES.QUALITYITEMTYPECOMPANYCODE = QUALITYLEVEL.ITEMTYPECOMPANYCODE AND WASTEGENERATIONTEMPLATES.ITEMTYPECODE = QUALITYLEVEL.ITEMTYPECODE AND WASTEGENERATIONTEMPLATES.QUALITYCODE = QUALITYLEVEL.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WASTEGENERATIONTEMPLATESUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ANALYSISTYPECODE,
       t.GROUPID,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.QUALITYITEMTYPECOMPANYCODE,
       t.QUALITYCODE,
       t.FLAG,
       t.PRODPRGTEMPLATECODE,
       t.STKTRANSTEMPLATECOMPANYCODE,
       t.STKTRANSTEMPLATECODE,
       t.WAREHOUSECOMPANYCODE
FROM   DB2ADMIN.WASTEGENERATIONTEMPLATES t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
