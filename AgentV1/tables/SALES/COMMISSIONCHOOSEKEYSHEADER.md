# DB2ADMIN.COMMISSIONCHOOSEKEYSHEADER

- **Module**: `SALES` (low confidence — FK neighbourhood: 2 of 2 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `COMPANYCODE`, `ORDERTYPE`, `TYPE`, `CODE`
- **FK degree**: referenced by 3 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 38496

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ORDERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 2 | `TYPE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 3 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `COMMISSIONCHOOSEKEYSHEADER.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `COMMISSIONCHOOSEKEYSHEADER_COMMISSIONCHOOSEKEYS` | [`COMMISSIONCHOOSEKEYS`](../SALES/COMMISSIONCHOOSEKEYS.md) | `CMSCHSKEYSHEADERCOMPANYCODE`, `CMSCHOOSEKEYSHEADERORDERTYPE`, `COMMISSIONCHOOSEKEYSHEADERTYPE`, `COMMISSIONCHOOSEKEYSHEADERCODE` | `COMMISSIONCHOOSEKEYS.CMSCHSKEYSHEADERCOMPANYCODE = COMMISSIONCHOOSEKEYSHEADER.COMPANYCODE AND COMMISSIONCHOOSEKEYS.CMSCHOOSEKEYSHEADERORDERTYPE = COMMISSIONCHOOSEKEYSHEADER.ORDERTYPE AND COMMISSIONCHOOSEKEYS.COMMISSIONCHOOSEKEYSHEADERTYPE = COMMISSIONCHOOSEKEYSHEADER.TYPE AND COMMISSIONCHOOSEKEYS.COMMISSIONCHOOSEKEYSHEADERCODE = COMMISSIONCHOOSEKEYSHEADER.CODE` |
| `COMMISSIONCHOOSEKEYSHEADER_COMMISSIONCHOOSEKEYS` | [`SALESORDERTEMPLATE`](../SALES/SALESORDERTEMPLATE.md) | `COMPANYCODE`, `ORDERTYPE`, `COMMISSIONCHOOSEKEYSTYPE`, `COMMISSIONCHOOSEKEYSCODE` | `SALESORDERTEMPLATE.COMPANYCODE = COMMISSIONCHOOSEKEYSHEADER.COMPANYCODE AND SALESORDERTEMPLATE.ORDERTYPE = COMMISSIONCHOOSEKEYSHEADER.ORDERTYPE AND SALESORDERTEMPLATE.COMMISSIONCHOOSEKEYSTYPE = COMMISSIONCHOOSEKEYSHEADER.TYPE AND SALESORDERTEMPLATE.COMMISSIONCHOOSEKEYSCODE = COMMISSIONCHOOSEKEYSHEADER.CODE` |
| `COMMISSIONCHOOSEKEYSHEADER_COMMISSIONCHOOSEKEYS` | [`SALESORDERLINETEMPLATE`](../SALES/SALESORDERLINETEMPLATE.md) | `COMPANYCODE`, `ORDERTYPE`, `COMMISSIONCHOOSEKEYSTYPE`, `COMMISSIONCHOOSEKEYSCODE` | `SALESORDERLINETEMPLATE.COMPANYCODE = COMMISSIONCHOOSEKEYSHEADER.COMPANYCODE AND SALESORDERLINETEMPLATE.ORDERTYPE = COMMISSIONCHOOSEKEYSHEADER.ORDERTYPE AND SALESORDERLINETEMPLATE.COMMISSIONCHOOSEKEYSTYPE = COMMISSIONCHOOSEKEYSHEADER.TYPE AND SALESORDERLINETEMPLATE.COMMISSIONCHOOSEKEYSCODE = COMMISSIONCHOOSEKEYSHEADER.CODE` |

## Indexes

- `COMMISSIONCHOOSEKEYSHEADERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ORDERTYPE,
       t.TYPE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID
FROM   DB2ADMIN.COMMISSIONCHOOSEKEYSHEADER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
