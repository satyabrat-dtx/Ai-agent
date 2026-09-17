# DB2ADMIN.QUALITYTEMPLATE

- **Module**: `QUALITY` (high confidence — table name starts with 'QUALITY')
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 2 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 98233

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(5) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 3 | `SUBCODE01CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 4 | `SUBCODE02CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 5 | `SUBCODE03CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 6 | `SUBCODE04CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 7 | `SUBCODE05CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 8 | `SUBCODE06CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 9 | `SUBCODE07CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 10 | `SUBCODE08CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 11 | `SUBCODE09CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 12 | `SUBCODE10CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 18 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 19 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 20 | `LOGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 21 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 22 | `TERMSOFLOGCODE` | CHAR(2) |  | FK | foreign_key |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `QUALITYTEMPLATE.COMPANYCODE = COMPANY.CODE` |
| `TERMSOFLOG_TERMSOFLOG` | `COMPANYCODE`, `TERMSOFLOGORDERTYPE`, `TERMSOFLOGCODE` | [`TERMSOFLOG`](../CORE_MASTER/TERMSOFLOG.md) | `COMPANYCODE`, `ORDERTYPE`, `CODE` | RESTRICT | `QUALITYTEMPLATE.COMPANYCODE = TERMSOFLOG.COMPANYCODE AND QUALITYTEMPLATE.TERMSOFLOGORDERTYPE = TERMSOFLOG.ORDERTYPE AND QUALITYTEMPLATE.TERMSOFLOGCODE = TERMSOFLOG.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `QUALITYTEMPLATE_TEMPLATE` | [`QAGROUP`](../QUALITY/QAGROUP.md) | `COMPANYCODE`, `TEMPLATECODE` | `QAGROUP.COMPANYCODE = QUALITYTEMPLATE.COMPANYCODE AND QAGROUP.TEMPLATECODE = QUALITYTEMPLATE.CODE` |
| `QUALITYTEMPLATE_TEMPLATE` | [`QUALITYHEADER`](../QUALITY/QUALITYHEADER.md) | `COMPANYCODE`, `TEMPLATECODE` | `QUALITYHEADER.COMPANYCODE = QUALITYTEMPLATE.COMPANYCODE AND QUALITYHEADER.TEMPLATECODE = QUALITYTEMPLATE.CODE` |

## Indexes

- `QUALITYTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.ITEMTYPECODE,
       t.SUBCODE01CONTROLLED,
       t.SUBCODE02CONTROLLED,
       t.SUBCODE03CONTROLLED,
       t.SUBCODE04CONTROLLED,
       t.SUBCODE05CONTROLLED,
       t.SUBCODE06CONTROLLED,
       t.SUBCODE07CONTROLLED,
       t.SUBCODE08CONTROLLED,
       t.SUBCODE09CONTROLLED
FROM   DB2ADMIN.QUALITYTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
