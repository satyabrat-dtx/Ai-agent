# DB2ADMIN.TNAACTIVITYRESULTTYPE

- **Module**: `TNA` (low confidence — table name starts with 'TNA')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `COMPANYCODE`, `CODE`, `UNIQUEID`
- **FK degree**: referenced by 2 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 195343

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 11 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `TNAACTIVITYRESULTTYPE.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `TNAACTIVITYRESULTTYPE_ACTIVITYRESULTTYPE` | [`TNAACTIVITYDETAIL`](../TNA/TNAACTIVITYDETAIL.md) | `TNAACTIVITYTNAHDRCOMPANYCODE`, `ACTIVITYRESULTTYPECODE`, `TNAACTIVITYUNIQUEID` | `TNAACTIVITYDETAIL.TNAACTIVITYTNAHDRCOMPANYCODE = TNAACTIVITYRESULTTYPE.COMPANYCODE AND TNAACTIVITYDETAIL.ACTIVITYRESULTTYPECODE = TNAACTIVITYRESULTTYPE.CODE AND TNAACTIVITYDETAIL.TNAACTIVITYUNIQUEID = TNAACTIVITYRESULTTYPE.UNIQUEID` |
| `TNAACTIVITYRESULTTYPE_RESULTS` | [`TNAACTIVITYRESULT`](../TNA/TNAACTIVITYRESULT.md) | `TNAACTIVITYRESULTTYPECMYCODE`, `TNAACTIVITYRESULTTYPECODE`, `TNAACTIVITYRESULTTYPEUNIQUEID` | `TNAACTIVITYRESULT.TNAACTIVITYRESULTTYPECMYCODE = TNAACTIVITYRESULTTYPE.COMPANYCODE AND TNAACTIVITYRESULT.TNAACTIVITYRESULTTYPECODE = TNAACTIVITYRESULTTYPE.CODE AND TNAACTIVITYRESULT.TNAACTIVITYRESULTTYPEUNIQUEID = TNAACTIVITYRESULTTYPE.UNIQUEID` |

## Indexes

- `TNAACTIVITYRESULTTYPEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.UNIQUEID,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.TNAACTIVITYRESULTTYPE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
