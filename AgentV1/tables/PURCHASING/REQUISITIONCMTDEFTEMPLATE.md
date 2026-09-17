# DB2ADMIN.REQUISITIONCMTDEFTEMPLATE

- **Module**: `PURCHASING` (low confidence — FK neighbourhood: 1 of 1 related tables are PURCHASING)
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `COMPANYCODE`, `COMMENTTYPE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 120136

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `COMMENTTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 2 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `DIVISIONREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 7 | `REQUISITIONTEMPLATEREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 8 | `ITEMTYPEREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 9 | `ITEMREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 10 | `PURORDERTEMPLATEREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 11 | `PURORDERLINETEMPLATEREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 12 | `SUPPLIERREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `REQUISITIONCMTDEFTEMPLATE.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `REQUISITIONCMTDEFTEMPLATE_TEMPLATE` | [`REQUISITIONCOMMENTDEFINITION`](../PURCHASING/REQUISITIONCOMMENTDEFINITION.md) | `COMPANYCODE`, `COMMENTTYPE`, `TEMPLATECODE` | `REQUISITIONCOMMENTDEFINITION.COMPANYCODE = REQUISITIONCMTDEFTEMPLATE.COMPANYCODE AND REQUISITIONCOMMENTDEFINITION.COMMENTTYPE = REQUISITIONCMTDEFTEMPLATE.COMMENTTYPE AND REQUISITIONCOMMENTDEFINITION.TEMPLATECODE = REQUISITIONCMTDEFTEMPLATE.CODE` |

## Indexes

- `REQUISITIONCMTDEFTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.COMMENTTYPE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.DIVISIONREQUIRED,
       t.REQUISITIONTEMPLATEREQUIRED,
       t.ITEMTYPEREQUIRED,
       t.ITEMREQUIRED,
       t.PURORDERTEMPLATEREQUIRED,
       t.PURORDERLINETEMPLATEREQUIRED
FROM   DB2ADMIN.REQUISITIONCMTDEFTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
