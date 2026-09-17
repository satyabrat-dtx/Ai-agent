# DB2ADMIN.FINDOCUMENTTYPE

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `CODE`
- **FK degree**: referenced by 6 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 175178

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 2 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 3 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 4 | `ASSET` | SMALLINT | NOT NULL |  |  |  |
| 5 | `ACCOUNTSPAYABLE` | SMALLINT | NOT NULL |  |  |  |
| 6 | `ACCOUNTSRECEIVABLE` | SMALLINT | NOT NULL |  |  |  |
| 7 | `EMPLOYEE` | SMALLINT | NOT NULL |  |  |  |
| 8 | `BANK` | SMALLINT | NOT NULL |  |  |  |
| 9 | `CASH` | SMALLINT | NOT NULL |  |  |  |
| 10 | `MATERIAL` | SMALLINT | NOT NULL |  |  |  |
| 11 | `OTHERAP` | SMALLINT | NOT NULL |  |  |  |
| 12 | `OTHERAR` | SMALLINT | NOT NULL |  |  |  |
| 13 | `GENERALLEDGER` | SMALLINT | NOT NULL |  |  |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 18 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 19 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 21 | `EXPORTFINANCE` | SMALLINT | NOT NULL |  |  |  |
| 22 | `LCPOSTING` | SMALLINT | NOT NULL |  |  |  |
| 23 | `LCPAYMENT` | SMALLINT | NOT NULL |  |  |  |
| 24 | `LOANS` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 6

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `FINDOCUMENTTYPE_DOCUMENTTYPE` | [`FINDOCUMENTTEMPLATE`](../FINANCE/FINDOCUMENTTEMPLATE.md) | `DOCUMENTTYPECODE` | `FINDOCUMENTTEMPLATE.DOCUMENTTYPECODE = FINDOCUMENTTYPE.CODE` |
| `FINDOCUMENTTYPE_DOCUMENTTYPE` | [`FINADVANCE`](../FINANCE/FINADVANCE.md) | `DOCUMENTTYPECODE` | `FINADVANCE.DOCUMENTTYPECODE = FINDOCUMENTTYPE.CODE` |
| `FINDOCUMENTTYPE_DOCUMENTTYPE` | [`FINDOCUMENT`](../FINANCE/FINDOCUMENT.md) | `DOCUMENTTYPECODE` | `FINDOCUMENT.DOCUMENTTYPECODE = FINDOCUMENTTYPE.CODE` |
| `FINDOCUMENTTYPE_DOCUMENTTYPE` | [`FINOPENDOCUMENTS`](../FINANCE/FINOPENDOCUMENTS.md) | `DOCUMENTTYPECODE` | `FINOPENDOCUMENTS.DOCUMENTTYPECODE = FINDOCUMENTTYPE.CODE` |
| `FINDOCUMENTTYPE_DOCUMENT` | [`FINLOANREPAYMENTM`](../FINANCE/FINLOANREPAYMENTM.md) | `DOCUMENTCODE` | `FINLOANREPAYMENTM.DOCUMENTCODE = FINDOCUMENTTYPE.CODE` |
| `FINDOCUMENTTYPE_DOCUMENTTYPE` | [`FINLOANCAPITALSR`](../FINANCE/FINLOANCAPITALSR.md) | `DOCUMENTTYPECODE` | `FINLOANCAPITALSR.DOCUMENTTYPECODE = FINDOCUMENTTYPE.CODE` |

## Indexes

- `FINDOCUMENTTYPEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ASSET,
       t.ACCOUNTSPAYABLE,
       t.ACCOUNTSRECEIVABLE,
       t.EMPLOYEE,
       t.BANK,
       t.CASH,
       t.MATERIAL,
       t.OTHERAP
FROM   DB2ADMIN.FINDOCUMENTTYPE t
FETCH FIRST 100 ROWS ONLY;
```
