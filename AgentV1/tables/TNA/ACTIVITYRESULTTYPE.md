# DB2ADMIN.ACTIVITYRESULTTYPE

- **Module**: `TNA` (low confidence — FK neighbourhood: 2 of 2 related tables are TNA)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 4 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 191181

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 10 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ACTIVITYRESULTTYPE.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 4

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ACTIVITYRESULTTYPE_ACTIVITYRESULTTYPE` | [`CUSTOMIZEDOPTIONS`](../TNA/CUSTOMIZEDOPTIONS.md) | `ACTIVITYRESULTTYPECOMPANYCODE`, `ACTIVITYRESULTTYPECODE` | `CUSTOMIZEDOPTIONS.ACTIVITYRESULTTYPECOMPANYCODE = ACTIVITYRESULTTYPE.COMPANYCODE AND CUSTOMIZEDOPTIONS.ACTIVITYRESULTTYPECODE = ACTIVITYRESULTTYPE.CODE` |
| `ACTIVITYRESULTTYPE_ACTIVITYRESULTTYPE` | [`TNADETAIL`](../TNA/TNADETAIL.md) | `TNAHEADERCOMPANYCODE`, `ACTIVITYRESULTTYPECODE` | `TNADETAIL.TNAHEADERCOMPANYCODE = ACTIVITYRESULTTYPE.COMPANYCODE AND TNADETAIL.ACTIVITYRESULTTYPECODE = ACTIVITYRESULTTYPE.CODE` |
| `ACTIVITYRESULTTYPE_ACTIVITYRESULTTYPE` | [`TNAHEADER`](../TNA/TNAHEADER.md) | `COMPANYCODE`, `ACTIVITYRESULTTYPECODE` | `TNAHEADER.COMPANYCODE = ACTIVITYRESULTTYPE.COMPANYCODE AND TNAHEADER.ACTIVITYRESULTTYPECODE = ACTIVITYRESULTTYPE.CODE` |
| `ACTIVITYRESULTTYPE_RESULTS` | [`ACTIVITYRESULT`](../TNA/ACTIVITYRESULT.md) | `ACTIVITYRESULTTYPECOMPANYCODE`, `ACTIVITYRESULTTYPECODE` | `ACTIVITYRESULT.ACTIVITYRESULTTYPECOMPANYCODE = ACTIVITYRESULTTYPE.COMPANYCODE AND ACTIVITYRESULT.ACTIVITYRESULTTYPECODE = ACTIVITYRESULTTYPE.CODE` |

## Indexes

- `ACTIVITYRESULTTYPEUID` (ABSUNIQUEID)

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
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ACTIVITYRESULTTYPE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
