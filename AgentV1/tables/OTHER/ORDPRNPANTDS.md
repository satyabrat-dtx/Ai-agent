# DB2ADMIN.ORDPRNPANTDS

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 22
- **Primary key**: `COMPANYCODE`, `TDSTEUSERGENERICGROUPTYPECODE`, `TDSTYPECODE`, `TDSCODE`, `TDSITAXCODE`, `PANNO`, `EXEMPTIONFROMDATE`
- **FK degree**: referenced by 1 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 218038

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `TDSTEUSERGENERICGROUPTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `TDSTYPECODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 3 | `TDSCODE` | CHAR(6) | NOT NULL | PK | primary_key |  |
| 4 | `TDSITAXCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `PANNO` | CHAR(30) | NOT NULL | PK | primary_key |  |
| 6 | `EXEMPTIONNUMBER` | CHAR(15) |  |  |  |  |
| 7 | `EXEMPTIONTAXPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 8 | `EXEMPTIONMAXAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 9 | `TILLDATEAMTCR` | DECIMAL(15,5) |  |  |  |  |
| 10 | `EXEMPTIONFROMDATE` | DATE | NOT NULL | PK | primary_key |  |
| 11 | `EXEMPTIONTODATE` | DATE |  |  |  |  |
| 12 | `EXCEMPTIONLIMITREACHED` | SMALLINT | NOT NULL |  |  |  |
| 13 | `DEFAULTLINE` | SMALLINT | NOT NULL |  |  |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 18 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 19 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 21 | `TILLDATEAMTEXCEMPTION` | DECIMAL(15,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ORDPRNPANTDS_LINE` | [`ORDPRNPANTDSDETAIL`](../OTHER/ORDPRNPANTDSDETAIL.md) | `ORDPRNPANTDSCOMPANYCODE`, `ORDPRNPANTDSTDSTEUSGENGRPTECOD`, `ORDPRNPANTDSTDSTYPECODE`, `ORDPRNPANTDSTDSCODE`, `ORDPRNPANTDSTDSITAXCODE`, `ORDPRNPANTDSPANNO`, `ORDPRNPANTDSEXEMPTIONFROMDATE` | `ORDPRNPANTDSDETAIL.ORDPRNPANTDSCOMPANYCODE = ORDPRNPANTDS.COMPANYCODE AND ORDPRNPANTDSDETAIL.ORDPRNPANTDSTDSTEUSGENGRPTECOD = ORDPRNPANTDS.TDSTEUSERGENERICGROUPTYPECODE AND ORDPRNPANTDSDETAIL.ORDPRNPANTDSTDSTYPECODE = ORDPRNPANTDS.TDSTYPECODE AND ORDPRNPANTDSDETAIL.ORDPRNPANTDSTDSCODE = ORDPRNPANTDS.TDSCODE AND ORDPRNPANTDSDETAIL.ORDPRNPANTDSTDSITAXCODE = ORDPRNPANTDS.TDSITAXCODE AND ORDPRNPANTDSDETAIL.ORDPRNPANTDSPANNO = ORDPRNPANTDS.PANNO AND ORDPRNPANTDSDETAIL.ORDPRNPANTDSEXEMPTIONFROMDATE = ORDPRNPANTDS.EXEMPTIONFROMDATE` |

## Indexes

- `ORDPRNPANTDSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.TDSTEUSERGENERICGROUPTYPECODE,
       t.TDSTYPECODE,
       t.TDSCODE,
       t.TDSITAXCODE,
       t.PANNO,
       t.EXEMPTIONNUMBER,
       t.EXEMPTIONTAXPERCENTAGE,
       t.EXEMPTIONMAXAMOUNT,
       t.TILLDATEAMTCR,
       t.EXEMPTIONFROMDATE,
       t.EXEMPTIONTODATE
FROM   DB2ADMIN.ORDPRNPANTDS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
