# DB2ADMIN.TAXTEMPLATEHEADER

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `COMPANYCODE`, `CODE`, `EFFECTIVEFROMDATE`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 125060

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `EFFECTIVEFROMDATE` | DATE | NOT NULL | PK | primary_key |  |
| 6 | `EFFECTIVETODATE` | DATE |  |  |  |  |
| 7 | `TEMPLATETYPE` | CHAR(2) | NOT NULL |  |  |  |
| 8 | `ROUNDOFFITAXCODE` | CHAR(3) |  |  |  |  |
| 9 | `ROUNDOFFTYPE` | INTEGER | NOT NULL |  |  |  |
| 10 | `ROUNDOFFAMOUNT` | DECIMAL(10,5) | NOT NULL |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `TAXTEMPLATEHEADER.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `TAXTEMPLATEHEADER_TAXTEMPLATEDETAIL` | [`TAXTEMPLATEDETAIL`](../OTHER/TAXTEMPLATEDETAIL.md) | `TAXTEMPLATEHEADERCOMPANYCODE`, `TAXTEMPLATEHEADERCODE`, `TAXTMPHEADEREFFECTIVEFROMDATE` | `TAXTEMPLATEDETAIL.TAXTEMPLATEHEADERCOMPANYCODE = TAXTEMPLATEHEADER.COMPANYCODE AND TAXTEMPLATEDETAIL.TAXTEMPLATEHEADERCODE = TAXTEMPLATEHEADER.CODE AND TAXTEMPLATEDETAIL.TAXTMPHEADEREFFECTIVEFROMDATE = TAXTEMPLATEHEADER.EFFECTIVEFROMDATE` |

## Indexes

- `TAXTEMPLATEHEADERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.EFFECTIVEFROMDATE,
       t.EFFECTIVETODATE,
       t.TEMPLATETYPE,
       t.ROUNDOFFITAXCODE,
       t.ROUNDOFFTYPE,
       t.ROUNDOFFAMOUNT,
       t.CREATIONDATETIME
FROM   DB2ADMIN.TAXTEMPLATEHEADER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
